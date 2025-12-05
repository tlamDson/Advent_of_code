def solve_gift_shop_part2(input_data):
    cleaned_input = input_data.replace('\n', '').replace(' ', '')
    ranges_str = cleaned_input.split(',')
    
    total_invalid_sum = 0
    
    for r_str in ranges_str:
        if not r_str: continue
        
        try:
            start_s, end_s = r_str.split('-')
            start = int(start_s)
            end = int(end_s)
        except ValueError:
            continue
            
        for num in range(start, end + 1):
            if is_repeated_pattern(num):
                total_invalid_sum += num
                
    return total_invalid_sum

def is_repeated_pattern(num):
    s = str(num)
    length = len(s)
    for L in range(1, (length // 2) + 1):
        if length % L == 0:
            pattern = s[:L]
            repetitions = length // L
            if pattern * repetitions == s:
                return True
                
    return False

real_input = "./Day_2/input_day_2.txt"

if len(real_input.strip()) > 0:
    with open(real_input.strip(), 'r') as file:
        input_data = file.read()
    print(f"Final Sum: {solve_gift_shop_part2(input_data)}")
else:
    print("\n(Paste your specific puzzle input into the 'real_input' variable)")