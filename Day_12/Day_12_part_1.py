import sys
import collections

class Shape:
    def __init__(self, id, coords):
        self.id = id
        self.variations = self._generate_variations(coords)
        self.area = len(coords)

    def _normalize(self, coords):
        if not coords:
            return frozenset()
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        return frozenset((r - min_r, c - min_c) for r, c in coords)

    def _generate_variations(self, original_coords):
        """Generate all 8 symmetry variations (4 rotations + horizontal flip)"""
        variations = set()
        current = original_coords
        transforms = []
        
        rots = [current]
        curr_rot = current
        for _ in range(3):
            curr_rot = {(c, -r) for r, c in curr_rot}
            rots.append(curr_rot)
            
        transforms.extend(rots)
        
        for r_set in rots:
            flipped = {(r, -c) for r, c in r_set}
            transforms.append(flipped)
            
        for t in transforms:
            variations.add(self._normalize(t))
            
        return list(variations)

def parse_input(data):
    lines = data.strip().split('\n')
    shapes = {}
    regions = []
    
    current_shape_id = None
    current_shape_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        if ':' in line:
            header = line.split(':')[0]
            if 'x' in header:
                parts = line.split(':')
                dims = parts[0].split('x')
                width, height = int(dims[0]), int(dims[1])
                counts = list(map(int, parts[1].strip().split()))
                regions.append({
                    'width': width,
                    'height': height,
                    'counts': counts
                })
            else:
                if current_shape_id is not None:
                    shapes[current_shape_id] = _build_shape(current_shape_id, current_shape_lines)
                    current_shape_lines = []
                
                current_shape_id = int(header)
                i += 1
                while i < len(lines):
                    shape_line = lines[i].rstrip()
                    if not shape_line or ':' in shape_line:
                        i -= 1
                        break
                    current_shape_lines.append(shape_line)
                    i += 1
        i += 1
        
    if current_shape_id is not None and current_shape_lines:
        shapes[current_shape_id] = _build_shape(current_shape_id, current_shape_lines)
        
    return shapes, regions

def _build_shape(id, lines):
    coords = set()
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == '#':
                coords.add((r, c))
    return Shape(id, coords)

def solve_region(width, height, required_pieces, shapes):
    """Solve tiling puzzle using backtracking with bitmask optimization"""
    placements = {}
    unique_shape_ids = set(required_pieces)
    
    for sid in unique_shape_ids:
        shape = shapes[sid]
        valid_masks = []
        
        for variant in shape.variations:
            v_rows = max(r for r, c in variant) + 1
            v_cols = max(c for r, c in variant) + 1
            
            for r in range(height - v_rows + 1):
                for c in range(width - v_cols + 1):
                    mask = 0
                    for (vr, vc) in variant:
                        grid_r, grid_c = r + vr, c + vc
                        bit_index = grid_r * width + grid_c
                        mask |= (1 << bit_index)
                    valid_masks.append(mask)
        
        placements[sid] = sorted(list(set(valid_masks)))
        
        if not placements[sid]:
            return False

    required_pieces.sort(key=lambda x: (shapes[x].area, x), reverse=True)
    
    total_area = sum(shapes[sid].area for sid in required_pieces)
    if total_area > width * height:
        return False

    n_pieces = len(required_pieces)
    target_mask = (1 << (width * height)) - 1
    memo = {}

    def backtrack(idx, current_mask, last_move_idx):
        if idx == n_pieces:
            return True
            
        remaining_area = sum(shapes[required_pieces[i]].area for i in range(idx, n_pieces))
        empty_cells = bin(current_mask ^ target_mask).count('1')
        if remaining_area > empty_cells:
            return False
            
        state = (idx, current_mask)
        if state in memo:
            return memo[state]
            
        sid = required_pieces[idx]
        possible_moves = placements[sid]
        
        start_i = 0
        if idx > 0 and required_pieces[idx] == required_pieces[idx-1]:
            start_i = last_move_idx + 1
            
        for i in range(start_i, len(possible_moves)):
            move_mask = possible_moves[i]
            
            if (current_mask & move_mask) == 0:
                if backtrack(idx + 1, current_mask | move_mask, i):
                    memo[state] = True
                    return True
        
        memo[state] = False
        return False

    return backtrack(0, 0, -1)

def main(input_str):
    shapes, regions = parse_input(input_str)
    
    solvable_count = 0
    
    for i, region in enumerate(regions):
        required = []
        counts = region['counts']
        for sid, count in enumerate(counts):
            required.extend([sid] * count)
            
        if not required:
            solvable_count += 1
            continue
            
        possible = True
        for sid in required:
            if sid not in shapes:
                possible = False
                break
        
        if possible and solve_region(region['width'], region['height'], required, shapes):
            solvable_count += 1
            
    return solvable_count

real_input = "./Day_12/input.txt"

with open(real_input, 'r') as f:
    content = f.read()
print(f"Answer: {main(content)}")

#Answer : 425