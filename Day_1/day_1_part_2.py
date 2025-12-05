def solve_safe_dial_part2(input_data):
    current_pos = 50
    total_zeros = 0
    
    instructions = input_data.strip().split('\n')
    
    for instruction in instructions:
        if not instruction: continue 
        
        direction = instruction[0]    
        amount = int(instruction[1:])   
        
        if direction == 'R':
            target_val = current_pos + amount
            zeros_passed = (target_val // 100) - (current_pos // 100)
            
            total_zeros += zeros_passed
            current_pos = target_val % 100
            
        elif direction == 'L':
            target_val = current_pos - amount
            zeros_passed = ((current_pos - 1) // 100) - ((target_val - 1) // 100)
            
            total_zeros += zeros_passed
            current_pos = target_val % 100
            
    return total_zeros

real_input = "./Day_1/input.txt"

if len(real_input.strip()) > 0:
    with open(real_input.strip(), 'r') as file:
        input_data = file.read()
    print(f"Final: {solve_safe_dial_part2(input_data)}")
else:
    print("\n(Paste your specific puzzle input into the 'real_input' variable to get the final answer)")

#Final : 6475