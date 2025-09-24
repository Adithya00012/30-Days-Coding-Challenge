def count_negatives(grid):
    m = len(grid)
    n = len(grid[0])
    count = 0
    row, col = 0, n - 1
    
    while row < m and col >= 0:
        if grid[row][col] < 0:
            count += (m - row)
            col -= 1
        else:
            row += 1
            
    return count
