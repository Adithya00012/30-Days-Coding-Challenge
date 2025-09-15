def minimize_max_value(grid):
    m = len(grid)
    n = len(grid[0])

    cells = []
    for r in range(m):
        for c in range(n):
            cells.append((grid[r][c], r, c))
    
    cells.sort()
    result = [[0] * n for _ in range(m)]
    max_row_val = [0] * m
    max_col_val = [0] * n
    
    for val, r, c in cells:
        new_val = max(max_row_val[r], max_col_val[c]) + 1
        result[r][c] = new_val
        max_row_val[r] = new_val
        max_col_val[c] = new_val
        
    return result
