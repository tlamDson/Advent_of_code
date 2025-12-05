def solve_lobby_part2(input_data):
    lines = input_data.strip().split('\n')
    total_joltage = 0
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line: continue
        
        max_bank_val = get_max_subsequence(stripped_line, 12)
        total_joltage += max_bank_val
        
    return total_joltage

def get_max_subsequence(bank, k):
    n = len(bank)
    if n < k: return 0
    
    drop_count = n - k
    stack = []
    
    for digit in bank:
        while drop_count > 0 and stack and stack[-1] < digit:
            stack.pop()
            drop_count -= 1
        stack.append(digit)
        
    result_digits = stack[:k]
    
    return int("".join(result_digits))

real_input = "./Day_3/input.txt"

with open(real_input, 'r') as file:
    input_data = file.read()

if len(input_data.strip()) > 0:
    print(f"Total Output Joltage: {solve_lobby_part2(input_data)}")
else:
    print("Input file is empty.")

#Total Output Joltage: 171518260283767