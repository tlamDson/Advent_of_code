import re

def solve_trash_compactor(input_data):
    lines = [line for line in input_data.split('\n') if line]
    
    if not lines:
        return "Error: Empty input."

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    active_beams = set()
    start_row = -1
    
    for r, line in enumerate(padded_lines):
        if 'S' in line:
            active_beams.add(line.index('S'))
            start_row = r
            break
            
    if start_row == -1:
        return 0
        
    split_count = 0
    
    for r in range(start_row + 1, len(padded_lines)):
        if not active_beams:
            break
            
        next_beams = set()
        current_line = padded_lines[r]
        
        for col in active_beams:
            if col < 0 or col >= max_len:
                continue
                
            char = current_line[col]
            
            if char == '^':
                split_count += 1
                next_beams.add(col - 1)
                next_beams.add(col + 1)
            else:
                next_beams.add(col)
        
        active_beams = next_beams

    return split_count

real_input = "./Day_7/input.txt"

with open(real_input, 'r') as file:
    input_data = file.read()

print(solve_trash_compactor(input_data))

#Answer : 1507