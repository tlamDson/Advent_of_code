def solve_trash_compactor_part2(input_data):
    lines = [line for line in input_data.split('\n') if line]
    
    if not lines:
        return "Error: Empty input."

    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    
    grand_total = 0
    
    current_block_columns = []
    
    for col_idx in range(max_len):
        col_str = "".join(padded_lines[row][col_idx] for row in range(len(padded_lines)))
        
        if col_str.strip() == "":
            if current_block_columns:
                grand_total += calculate_block_vertical(current_block_columns)
                current_block_columns = []
        else:
            current_block_columns.append(col_str)
            
    if current_block_columns:
        grand_total += calculate_block_vertical(current_block_columns)

    return grand_total

def calculate_block_vertical(columns):
    numbers = []
    operator = None
    
    for col_str in columns:
        if '+' in col_str:
            operator = '+'
        elif '*' in col_str:
            operator = '*'
            
        clean_str = col_str.replace(' ', '').replace('+', '').replace('*', '')
        
        if clean_str:
            numbers.append(int(clean_str))
            
    if operator == '+':
        return sum(numbers)
    elif operator == '*':
        result = 1
        for num in numbers:
            result *= num
        return result
        
    return 0


real_input = "./Day_6/input.txt"

with open(real_input, 'r') as file:
        input_data = file.read()
    
print(solve_trash_compactor_part2(input_data))

#Answer : 10194584711842