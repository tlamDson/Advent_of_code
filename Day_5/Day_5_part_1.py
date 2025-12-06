def solve_cafeteria_part1(input_data):
    try:
        parts = input_data.strip().split('\n\n')
        ranges_lines = parts[0].strip().split('\n')
        ids_lines = parts[1].strip().split('\n')
    except IndexError:
        return "Error: Input format invalid. Ensure there is a blank line between ranges and IDs."

    fresh_ranges = []
    for line in ranges_lines:
        start_s, end_s = line.split('-')
        fresh_ranges.append((int(start_s), int(end_s)))

    available_ids = [int(line) for line in ids_lines]

    fresh_count = 0

    for ing_id in available_ids:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ing_id <= end:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

    return fresh_count


real_input = "./Day_5/input.txt"

with open(real_input, 'r') as file:
    input_data = file.read()

print(solve_cafeteria_part1(input_data))

#Answer : 855