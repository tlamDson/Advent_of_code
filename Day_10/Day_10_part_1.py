import re
import itertools

def solve_factory(input_data):
    lines = input_data.strip().split('\n')
    total_presses = 0
    
    for line in lines:
        if not line.strip(): continue
        
        match_lights = re.search(r'\[([.#]+)\]', line)
        if not match_lights: continue
        target_str = match_lights.group(1)
        target_vec = [1 if c == '#' else 0 for c in target_str]
        num_lights = len(target_vec)
        
        button_specs = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        for spec in button_specs:
            indices = [int(x) for x in spec.split(',')]
            btn_vec = [0] * num_lights
            for idx in indices:
                if 0 <= idx < num_lights:
                    btn_vec[idx] = 1
            buttons.append(btn_vec)
            
        presses = solve_machine(target_vec, buttons)
        total_presses += presses
        
    return total_presses

def solve_machine(target, buttons):
    num_rows = len(target)
    num_cols = len(buttons)
    
    matrix = []
    for r in range(num_rows):
        row = [b[r] for b in buttons] + [target[r]]
        matrix.append(row)
        
    pivot_row = 0
    pivot_cols = []
    
    for col in range(num_cols):
        if pivot_row >= num_rows: break
        
        selected_row = -1
        for r in range(pivot_row, num_rows):
            if matrix[r][col] == 1:
                selected_row = r
                break
        
        if selected_row == -1:
            continue
            
        matrix[pivot_row], matrix[selected_row] = matrix[selected_row], matrix[pivot_row]
        
        for r in range(num_rows):
            if r != pivot_row and matrix[r][col] == 1:
                for c in range(col, num_cols + 1):
                    matrix[r][c] ^= matrix[pivot_row][c]
                    
        pivot_cols.append(col)
        pivot_row += 1

    for r in range(num_rows):
        if matrix[r][num_cols] == 1 and all(v == 0 for v in matrix[r][:num_cols]):
            return 0
            
    free_cols = [c for c in range(num_cols) if c not in pivot_cols]
    min_presses = float('inf')
    
    for free_vals in itertools.product([0, 1], repeat=len(free_cols)):
        solution = [0] * num_cols
        
        for i, f_col in enumerate(free_cols):
            solution[f_col] = free_vals[i]
            
        for r, p_col in enumerate(pivot_cols):
            val = matrix[r][num_cols]
            
            for f_col in free_cols:
                if matrix[r][f_col] == 1:
                    val ^= solution[f_col]
            
            solution[p_col] = val
            
        weight = sum(solution)
        if weight < min_presses:
            min_presses = weight
            
    return min_presses if min_presses != float('inf') else 0


with open("./Day_10/input.txt", 'r') as file:
    input_data = file.read()
print(f"Answer: {solve_factory(input_data)}")

# Answer : 449