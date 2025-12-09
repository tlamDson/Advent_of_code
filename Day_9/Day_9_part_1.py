def solve_movie_theater(input_data):
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    points = []
    
    for line in lines:
        try:
            parts = list(map(int, line.split(',')))
            points.append(tuple(parts))
        except ValueError:
            continue

    n = len(points)
    if n < 2:
        return 0

    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            
            width = abs(p1[0] - p2[0]) + 1
            height = abs(p1[1] - p2[1]) + 1
            
            area = width * height
            
            if area > max_area:
                max_area = area

    return max_area

real_input = "./Day_9/input.txt"

try:
    with open(real_input, 'r') as file:
        input_data = file.read()
    print(solve_movie_theater(input_data))
except FileNotFoundError:
    print(f"File not found. Running Example:")

#Answer : 4760959496