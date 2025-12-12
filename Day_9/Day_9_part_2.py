def solve_movie_theater_sparse(input_data):
    
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    points = []
    
    for line in lines:
        try:
            parts = list(map(int, line.split(',')))
            points.append(tuple(parts))
        except ValueError:
            continue

    n = len(points)
    xs = sorted(list(set(p[0] for p in points)))
    ys = sorted(list(set(p[1] for p in points)))
    
    x_map = {x: i for i, x in enumerate(xs)}
    y_map = {y: i for i, y in enumerate(ys)}
    
    W = len(xs)
    H = len(ys)
    
    grid = [[0] * (W - 1) for _ in range(H - 1)]
    
    v_edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        
        if p1[0] == p2[0]:
            y_min, y_max = sorted((p1[1], p2[1]))
            v_edges.append((p1[0], y_min, y_max))

    for j in range(H - 1):
        active_edges = []
        current_y_bottom = ys[j]
        
        for vx, v_ymin, v_ymax in v_edges:
            if v_ymin <= current_y_bottom and v_ymax > current_y_bottom:
                active_edges.append(vx)
        
        active_edges.sort()
        
        is_inside = False
        for k in range(len(active_edges) - 1):
            is_inside = not is_inside
            
            if is_inside:
                x_start_idx = x_map[active_edges[k]]
                x_end_idx = x_map[active_edges[k+1]]
                
                for xi in range(x_start_idx, x_end_idx):
                    grid[j][xi] = 1

    p_sum = [[0] * (W - 1) for _ in range(H - 1)]
    
    for j in range(H - 1):
        for i in range(W - 1):
            val = grid[j][i]
            top = p_sum[j-1][i] if j > 0 else 0
            left = p_sum[j][i-1] if i > 0 else 0
            top_left = p_sum[j-1][i-1] if (j > 0 and i > 0) else 0
            p_sum[j][i] = val + top + left - top_left

    def get_grid_sum(idx_x1, idx_y1, idx_x2, idx_y2):
        if idx_x1 > idx_x2 or idx_y1 > idx_y2:
            return 0
        
        res = p_sum[idx_y2][idx_x2]
        if idx_y1 > 0: res -= p_sum[idx_y1-1][idx_x2]
        if idx_x1 > 0: res -= p_sum[idx_y2][idx_x1-1]
        if idx_y1 > 0 and idx_x1 > 0: res += p_sum[idx_y1-1][idx_x1-1]
        return res

    max_area = 0
    
    for i in range(n):
        for k in range(i + 1, n):
            p1 = points[i]
            p2 = points[k]
            
            ix1, iy1 = x_map[p1[0]], y_map[p1[1]]
            ix2, iy2 = x_map[p2[0]], y_map[p2[1]]
            
            left_idx, right_idx = min(ix1, ix2), max(ix1, ix2)
            top_idx, bottom_idx = min(iy1, iy2), max(iy1, iy2)
            
            check_x2 = right_idx - 1
            check_y2 = bottom_idx - 1
            
            width_real = abs(p1[0] - p2[0]) + 1
            height_real = abs(p1[1] - p2[1]) + 1
            area = width_real * height_real
            
            if area <= max_area:
                continue

            expected_blocks = (check_x2 - left_idx + 1) * (check_y2 - top_idx + 1)
            
            if expected_blocks <= 0:
                max_area = area
            else:
                actual_sum = get_grid_sum(left_idx, top_idx, check_x2, check_y2)
                if actual_sum == expected_blocks:
                    max_area = area

    return max_area
real_input = "./Day_9/input.txt"

try:
    with open(real_input, 'r') as file:
        input_data = file.read()
    print(solve_movie_theater_sparse(input_data))
except FileNotFoundError:
    print("File not found.")

#Answer : 1343576598