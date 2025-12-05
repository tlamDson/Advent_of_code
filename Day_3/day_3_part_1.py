def solve_lobby(input_data):
    lines = input_data.strip().split('\n')
    total_joltage = 0
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line: continue
        
        max_bank_val = get_max_joltage(stripped_line)
        total_joltage += max_bank_val
        
    return total_joltage

def get_max_joltage(bank):
    max_val = -1
    n = len(bank)
    
    for i in range(n):
        for j in range(i + 1, n):
            val = int(bank[i] + bank[j])
            if val > max_val:
                max_val = val
                
    return max_val

real_input = "./Day_3/input.txt"

with open(real_input.strip(), 'r') as file:
    input_data = file.read()

if len(input_data.strip()) > 0:
    print(f"Total Output Joltage: {solve_lobby(input_data)}")
else:
    print("Input file is empty.")
    
#Total Output Joltage: 17330