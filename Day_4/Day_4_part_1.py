def solve_printing_department(input_data):
    grid = [list(line) for line in input_data.strip().split('\n')]
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    accessible_count = 0
    
    # Directions for 8 neighbors (row_offset, col_offset)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            # We only care if the current spot is a paper roll '@'
            if grid[r][c] == '@':
                neighbor_rolls = 0
                
                # Check all 8 adjacent cells
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check boundaries
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == '@':
                            neighbor_rolls += 1
                
                # Condition: fewer than 4 neighbors
                if neighbor_rolls < 4:
                    accessible_count += 1
                    
    return accessible_count

real_input = "./Day_4/input.txt"

with open(real_input, 'r') as f:
    print(solve_printing_department(f.read()))

#Answer : 1389