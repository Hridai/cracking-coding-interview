"""
Problem:
Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0.
"""

"""
Questions:
Does "set to 0" mean the original zeros too, or only cells that were non-zero?
(Standard interpretation: zero out the entire row and column regardless.)

Algorithm (O(M*N) time, O(M+N) extra space):
Two-pass approach using sets to track which rows and columns contain a zero.

Pass 1 — scan every cell; if zero, record its row index and col index in a set.
Pass 2 — scan every cell again; if its row or col is in either set, set it to 0.

Using sets (not lists) keeps membership checks O(1), giving overall O(M*N) time.
Extra space is O(M+N) for the two sets.

Time:  O(M*N)
Space: O(M+N) extra

---

O(1) space follow-up — "use the first row and column as markers":

Instead of separate sets, store the zero markers inside the matrix itself.
Row 0 serves as the "zero these columns" record.
Column 0 serves as the "zero these rows" record.

The catch: row 0 and col 0 are also part of the matrix, so we must check
whether they themselves originally contained a zero, BEFORE we start writing
markers into them. Two booleans capture this upfront.

Steps:
  1. zero_first_row = any zero exists in row 0?       (save before touching anything)
  2. zero_first_col = any zero exists in col 0?       (save before touching anything)
  3. Scan interior (r>=1, c>=1): if matrix[r][c]==0,
       set matrix[r][0] = 0  (mark row r)
       set matrix[0][c] = 0  (mark col c)
  4. Zero interior cells: if matrix[r][0]==0 or matrix[0][c]==0, zero that cell.
  5. If zero_first_row: zero all of row 0.
  6. If zero_first_col: zero all of col 0.

Steps 5 and 6 must come LAST — zeroing row 0 or col 0 early would corrupt the
markers written in step 3.

Time:  O(M*N)
Space: O(1) extra
"""

def zero_matrix(matrix_in):
    rows_with_zero = []
    cols_with_zero = []

    for row, rowval in enumerate(matrix_in):
        for col, colval in enumerate(rowval):
            if colval == 0:
                rows_with_zero.append(row)
                cols_with_zero.append(col)

    # we can do this in place, because lists are mutable.
    for row, rowval in enumerate(matrix_in):
        for col, colval in enumerate(rowval):
            if col in cols_with_zero:
                matrix_in[row][col] = 0
            if row in rows_with_zero:
                matrix_in[row][col] = 0
    
    return matrix_in


def zero_matrix_o1(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    # Step 1-2: check if the first row/col themselves need to be zeroed
    zero_first_row = any(matrix[0][c] == 0 for c in range(cols))
    zero_first_col = any(matrix[r][0] == 0 for r in range(rows))

    # Step 3: scan interior; write markers into row 0 and col 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # Step 4: zero interior cells based on markers
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # Steps 5-6: zero first row/col last, so markers aren't wiped early
    if zero_first_row:
        for c in range(cols):
            matrix[0][c] = 0

    if zero_first_col:
        for r in range(rows):
            matrix[r][0] = 0

    return matrix


def test_func(matrix_in, expected_result):
    original = [row[:] for row in matrix_in]  # snapshot before mutation
    res = zero_matrix(matrix_in)
    if res != expected_result:
        raise ValueError(f"Error: Running logic on {original} gives result: {res} which does not match {expected_result}!")


if __name__ == "__main__":
    test_func(
        [
            [1, 1, 1],
            [2, 0, 2],
            [3, 3, 3],
        ],
        [
            [1, 0, 1],
            [0, 0, 0],
            [3, 0, 3],
        ]
    )
