# Python Memory, Lists, and Why Append is O(1)

## How a Python List Works Under the Hood

A Python `list` is a **dynamic array** — at the C level, it's a contiguous block of memory with two key bookkeeping values:

- `length` — how many items are actually stored
- `capacity` — how large the allocated block is

When you append and `length == capacity`, Python:
1. Allocates a **new, larger block** (~1.125x or 2x the current capacity)
2. **Copies everything** from the old block to the new one
3. Discards the old block

The expensive step is the copy — O(n). But it happens rarely (only on resize), so the **amortised cost of append is O(1)**. The vast majority of appends are just:

```python
array[length] = x
length += 1
```

One write, one increment. That's it.

---

## Why Python Lists Use More Memory Than You'd Expect

A Python list does **not** store values directly. It stores **pointers** to Python objects.

```python
my_list = [0, 1, 2, 3]
```

In memory this looks like:

```
list array:  [ ptr, ptr, ptr, ptr ]
                |    |    |    |
                v    v    v    v
            int(0) int(1) int(2) int(3)   <-- scattered around the heap
```

Each Python `int` is not a raw number — it is a full Python object containing:
- A **reference count** (for garbage collection)
- A **pointer to its type** (`int`)
- The **actual value**

This overhead costs approximately **28 bytes per integer**.

---

## Python List vs Numpy: Concrete Memory Comparison

For 1,000,000 integers:

| | Python `list` | Numpy `int32` array |
|---|---|---|
| Pointer array | 8 MB (1M pointers × 8 bytes) | — |
| Object overhead | 28 MB (1M objects × 28 bytes) | — |
| Raw values | — | 4 MB (1M × 4 bytes) |
| **Total** | **~36 MB** | **~4 MB** |

**~9x more memory** for the Python list.

Numpy stores the raw bytes directly, packed tightly, with no object overhead and no pointers — because it knows every element is the same type upfront.

---

## The Cache Consequence

This memory layout has a performance consequence beyond just size.

**Numpy iteration:**
- Reads a single contiguous 4MB block
- The CPU prefetcher can predict exactly what memory is coming next
- Extremely cache-friendly

**Python list iteration:**
- Reads a pointer → jumps to a random heap address → reads the int object → comes back
- Repeats 1,000,000 times
- 1 million random memory jumps — the CPU cache gets thrashed constantly

This is why numpy array operations can be **100x faster** than equivalent Python list loops, even though both are "arrays." The algorithm is the same — the memory layout is the difference.

---

## The Tradeoff Python Chose

Python lists are optimised for **flexibility**, not raw performance:

- Mixed types in one list (`[1, "hello", 3.14]`) — only possible because everything is a pointer to an object
- Amortised O(1) append — fast for the common case
- At the cost of: higher memory use, pointer indirection, cache inefficiency

Numpy gives up flexibility (one type per array, fixed at creation) in exchange for raw memory and cache performance.

---

## How This Connects to the Three-in-One Problem

The Three-in-One problem (Chapter 3, Q1) asks you to implement three stacks inside a single array. This is directly analogous to how memory is managed at the OS/runtime level:

- You get one flat block (like calling `malloc(300)` in C)
- You subdivide it yourself with bookkeeping variables (partition boundaries, top pointers)
- There are no sub-objects — just index arithmetic on a flat array

This mental model — **flat memory + index arithmetic + bookkeeping** — is the foundation beneath every abstraction in Python, including the list itself.

The naive approach (fixed partitions) is essentially what Python's list does for a single stack: claim a region, track a top pointer, resize (or in this case, error out) when full.
