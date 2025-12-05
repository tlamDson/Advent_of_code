def solve_safe_dial_part_1(input_data):
    current_pos = 50
    zero_count = 0
    instructions = input_data.strip().split('\n')

    for instruction in instructions:
        if not instruction.strip():
            continue

        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == 'R':
            current_pos = (current_pos + amount) % 100
        elif direction == 'L':
            current_pos = (current_pos - amount) % 100

        if current_pos == 0:
            zero_count += 1

    return zero_count

def solve_safe_dial_from_file(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()

    return solve_safe_dial_part_1(input_data)

real_input = './Day_1/input.txt'

if "PASTE_YOUR_INPUT_HERE" not in real_input:
    print(f"Real Answer: {solve_safe_dial_from_file(real_input)}")
else:
    print("Please paste your puzzle input into the 'real_input' variable.")

