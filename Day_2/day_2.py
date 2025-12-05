def solve_gift_shop(input_data):
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
            s = str(num)
            length = len(s)
            
            if length % 2 != 0:
                continue
                
            mid = length // 2
            first_half = s[:mid]
            second_half = s[mid:]
            
            if first_half == second_half:
                total_invalid_sum += num
                
    return total_invalid_sum


real_input = "./Day_2/input_day_2.txt"

if len(real_input.strip()) > 0:
    with open(real_input.strip(), 'r') as file:
        input_data = file.read()
    print(f"Final Sum: {solve_gift_shop(input_data)}")
else:
    print("\n(Paste your specific puzzle input into the 'real_input' variable)")

#Final Sum: 18893502033