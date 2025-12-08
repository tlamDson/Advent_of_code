import re
from collections import defaultdict

def solve_quantum_manifold(input_data):
    lines = [line for line in input_data.split('\n') if line]
    
    if not lines:
        return "Error: Empty input."

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    timelines = defaultdict(int)
    start_row = -1
    
    for r, line in enumerate(padded_lines):
        if 'S' in line:
            timelines[line.index('S')] = 1
            start_row = r
            break
            
    if start_row == -1:
        return 0
        
    total_finished_timelines = 0
    
    for r in range(start_row + 1, len(padded_lines)):
        if not timelines:
            break
            
        next_timelines = defaultdict(int)
        current_line = padded_lines[r]
        
        for col, count in timelines.items():
            if col < 0 or col >= max_len:
                total_finished_timelines += count
                continue
                
            char = current_line[col]
            
            if char == '^':
                next_timelines[col - 1] += count
                next_timelines[col + 1] += count
            else:
                next_timelines[col] += count
        
        timelines = next_timelines

    total_finished_timelines += sum(timelines.values())

    return total_finished_timelines

real_input = "./Day_7/input.txt"

with open(real_input, 'r') as file:
    input_data = file.read()

print(solve_quantum_manifold(input_data))

# Answer : 1537373473728