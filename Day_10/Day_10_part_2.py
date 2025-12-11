import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve_factory(input_data):
    lines = input_data.strip().split('\n')
    total_presses = 0
    
    for line in lines:
        if not line.strip(): 
            continue
        
        match_joltage = re.search(r'\{([\d,]+)\}', line)
        if not match_joltage: 
            continue
        target_str = match_joltage.group(1)
        target_vec = [int(x) for x in target_str.split(',')]
        num_counters = len(target_vec)
        
        button_specs = re.findall(r'\(([\d,]+)\)', line)
        buttons = []
        for spec in button_specs:
            indices = [int(x) for x in spec.split(',')]
            btn_vec = [0] * num_counters
            for idx in indices:
                if 0 <= idx < num_counters:
                    btn_vec[idx] = 1
            if sum(btn_vec) > 0:
                buttons.append(btn_vec)
        
        min_presses = solve_machine(target_vec, buttons)
        if min_presses != float('inf'):
            total_presses += min_presses
        
    return int(total_presses)

def solve_machine(target, buttons):
    if not buttons:
        return float('inf')
    
    num_counters = len(target)
    num_buttons = len(buttons)
    
    A = np.zeros((num_counters, num_buttons))
    for btn_idx, btn in enumerate(buttons):
        for counter_idx in range(num_counters):
            A[counter_idx, btn_idx] = btn[counter_idx]
    
    b = np.array(target, dtype=float)
    c = np.ones(num_buttons)
    constraints = LinearConstraint(A, b, b)
    bounds = Bounds(lb=0, ub=np.inf)
    integrality = np.ones(num_buttons)
    
    result = milp(c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        return int(round(result.fun))
    
    return float('inf')

with open("./Day_10/input.txt", 'r') as file:
    input_data = file.read()
print(solve_factory(input_data))

#Answer : 17848