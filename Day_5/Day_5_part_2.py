def solve_cafeteria_part2(input_data):
    try:
        parts = input_data.strip().split('\n\n')
        ranges_lines = parts[0].strip().split('\n')
    except IndexError:
        return "Error: Input format invalid."

    raw_ranges = []
    for line in ranges_lines:
        if not line.strip():
            continue
        start_s, end_s = line.split('-')
        raw_ranges.append([int(start_s), int(end_s)])

    raw_ranges.sort(key=lambda x: x[0])

    merged_ranges = []

    for current_start, current_end in raw_ranges:
        if not merged_ranges:
            merged_ranges.append([current_start, current_end])
        else:
            last_start, last_end = merged_ranges[-1]

            if current_start <= last_end + 1:
                merged_ranges[-1][1] = max(last_end, current_end)
            else:
                merged_ranges.append([current_start, current_end])

    total_fresh_ids = 0
    for start, end in merged_ranges:
        total_fresh_ids += (end - start + 1)

    return total_fresh_ids


real_input = "./Day_5/input.txt"

with open(real_input.strip(), 'r') as file:
    input_data = file.read()

print(solve_cafeteria_part2(input_data))

# Answer : 348115621205535