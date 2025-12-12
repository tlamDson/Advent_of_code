def solve_printing_department_part2(input_data):
    # Parse grid into mutable list of lists
    grid = [list(line) for line in input_data.strip().split('\n')]
    if not grid:
        return 0
        
    rows = len(grid)
    cols = len(grid[0])
    total_removed = 0
    
    # Directions for 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    while True:
        to_remove = []
        
        # Scan the current state of the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    neighbor_rolls = 0
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        # Check bounds
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == '@':
                                neighbor_rolls += 1
                    
                    # Condition: fewer than 4 neighbors
                    if neighbor_rolls < 4:
                        to_remove.append((r, c))
        
        # If no rolls can be removed in this pass, we are done
        if not to_remove:
            break
            
        # Update total count
        total_removed += len(to_remove)
        
        # Remove the rolls (simultaneously)
        for r, c in to_remove:
            grid[r][c] = '.' # Mark as empty/removed
            
    return total_removed

real_input = "./Day_4/input.txt"

with open(real_input, 'r') as f:
    print(solve_printing_department_part2(f.read()))
    
#Answer : 9000