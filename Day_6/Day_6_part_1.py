import re

def solve_trash_compactor(input_data):
    lines = [line for line in input_data.split('\n') if line]
    
    if not lines:
        return "Error: Empty input."

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    grand_total = 0
    
    current_block_lines = [''] * len(padded_lines)
    block_has_content = False
    
    for col_idx in range(max_len):
        col_chars = [padded_lines[row][col_idx] for row in range(len(padded_lines))]
        
        is_separator = all(char == ' ' for char in col_chars)
        
        if is_separator:
            if block_has_content:
                grand_total += solve_single_problem(current_block_lines)
                
                current_block_lines = [''] * len(padded_lines)
                block_has_content = False
        else:
            block_has_content = True
            for row in range(len(padded_lines)):
                current_block_lines[row] += col_chars[row]
    
    if block_has_content:
        grand_total += solve_single_problem(current_block_lines)

    return grand_total

def solve_single_problem(block_lines):
    full_text = " ".join(block_lines)
    
    numbers = [int(n) for n in re.findall(r'\d+', full_text)]
    
    if not numbers:
        return 0

    if '*' in full_text:
        result = 1
        for num in numbers:
            result *= num
        return result
    elif '+' in full_text:
        return sum(numbers)
        
    return 0


real_input = "./Day_6/input.txt"

with open(real_input, 'r') as file:
        input_data = file.read()

print(solve_trash_compactor(input_data))

#Answer : 5782351442566