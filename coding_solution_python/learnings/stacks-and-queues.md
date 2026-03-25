# Stacks & Queues — Interview Cheat Sheet

---

## Core Concepts

### Stack — LIFO (Last In, First Out)
| Operation | Description | Complexity |
|-----------|-------------|------------|
| `push(x)` | Add to top | O(1) |
| `pop()` | Remove & return top | O(1) |
| `peek()` | Return top without removing | O(1) |
| `is_empty()` | Check if empty | O(1) |

### Queue — FIFO (First In, First Out)
| Operation | Description | Complexity |
|-----------|-------------|------------|
| `enqueue(x)` | Add to back | O(1) |
| `dequeue()` | Remove & return front | O(1) |
| `peek()` | Return front without removing | O(1) |
| `is_empty()` | Check if empty | O(1) |

---

## Implementation Choices & Tradeoffs

### Stack backed by linked list vs array
- **Linked list**: O(1) push/pop guaranteed, no overflow (dynamic), but pointer overhead per node
- **Array (fixed)**: O(1) push/pop, cache-friendly, but must handle overflow; Python list gives amortised O(1) append

### Queue backed by `collections.deque`
- Python's `deque` is a doubly-linked list under the hood — O(1) `appendleft`/`pop` from both ends
- Never implement a queue with a plain Python list — `list.pop(0)` is O(n) due to shifting

---

## The Classic Patterns

### 1. Two-Stack Queue (queue via stacks)
Simulate FIFO using two stacks: `stack_in` and `stack_out`.

- `enqueue(x)`: push to `stack_in` — O(1)
- `dequeue()`: if `stack_out` empty, pour all of `stack_in` into `stack_out` (reverses order), then pop `stack_out`

**Amortised O(1) dequeue** — each element is moved at most once in its lifetime.
Say this out loud in the interview: *"A single dequeue can be O(n), but amortised across all operations it's O(1) because each element crosses from stack_in to stack_out exactly once."*

```
stack_in:  [1, 2, 3]  ← 3 on top
pour →
stack_out: [3, 2, 1]  ← 1 on top  → pop → returns 1 (correct FIFO)
```

### 2. Min Stack (O(1) min at all times)
Shadow the main stack with a `min_stack` that stores the running minimum.

- `push(x)`: push x to main; push `min(x, min_stack.peek())` to min stack
- `pop()`: pop both stacks simultaneously
- `min()`: peek the min stack

Each slot in the min stack answers: *"what is the minimum of everything at or below this level?"*
Popping the current minimum automatically reveals the previous minimum.

**Common wrong answer**: storing a single `self.min` value — breaks when the minimum is popped.

### 3. Fixed-Partition Three-Stack Array
Divide a single array of size `3n` into three equal segments.
- Track a top pointer per stack, initialised to each segment's base index
- Overflow check: `top_pointer >= (stack_number + 1) * stack_size`
- Empty check: `top_pointer <= stack_number * stack_size`

**Follow-up the interviewer will ask**: *"What if the stacks need unequal space?"*
Answer: flexible partitioning — store `(value, prev_index)` pairs and maintain a free-list of available slots. O(1) ops still, but more complex bookkeeping.

### 4. Set of Stacks (stack of plates)
A Python list of sub-stacks, each capped at `threshold`.

- `push`: if last sub-stack is full, append a new one
- `pop`: pop from last sub-stack; if it's now empty, remove it from the list

**Follow-up — `popAt(index)`**: two approaches:
- **Lazy**: just pop from `stacks[index]`, leave it under-capacity. O(1) but breaks the "only last stack is partial" invariant.
- **Roll-down**: after popping from `stacks[i]`, shift the bottom of `stacks[i+1]` up to fill the gap, cascade rightward. O(k) where k = number of stacks to the right. Requires `pop_bottom()` — your basic Stack won't support this; need a deque.

State the tradeoff and let the interviewer guide which they want.

---

## Complexity Reminders

| Structure | push/enqueue | pop/dequeue | peek | min (MinStack) |
|-----------|-------------|-------------|------|----------------|
| Stack (linked list) | O(1) | O(1) | O(1) | — |
| MinStack | O(1) | O(1) | O(1) | O(1) |
| Two-Stack Queue | O(1) | O(1) amortised | O(1) amortised | — |
| SetOfStacks | O(1) amortised | O(1) amortised | O(1) | — |

**Space**: all of the above are O(n) total, O(n) extra for auxiliary structures (min stack, second stack). State both in the interview.

---

## Things Interviewers Actually Test

- **Can you reason about amortised complexity?** The two-stack queue and set-of-plates problems both hinge on this.
- **Do you think about the follow-up?** Every Chapter 3 problem has one. Solve the base case cleanly, then immediately ask/address the extension.
- **Do you know when your sentinel breaks?** If you use `None` to mark "empty", pushing `None` as a value corrupts your logic. Use a size counter instead.
- **Can you articulate the invariant?** E.g. for SetOfStacks: "only the last sub-stack may be partially filled." If `popAt` violates this, say so explicitly.
- **Do you distinguish total space from extra space?** An O(n) input that uses O(n) extra space is very different from one that uses O(1) extra.

---

## Python-Specific Notes

- `list` as a stack: `append()` / `pop()` — both O(1) amortised. Fine for interviews.
- `collections.deque` as a queue: `append()` / `popleft()` — both O(1). Always prefer over `list` for queue use.
- Never use `list.pop(0)` — it's O(n).
- Python has no built-in stack/queue class. `queue.Queue` exists but is thread-safe and slower — not what interviewers mean.
- String immutability: irrelevant for stack/queue problems but watch for it in Chapter 1.
