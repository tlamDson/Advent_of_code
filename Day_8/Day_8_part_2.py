import re

def solve_playground_part2(input_data):
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    points = []
    
    for line in lines:
        parts = list(map(int, line.split(',')))
        points.append(tuple(parts))

    n = len(points)
    if n < 2:
        return 0

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist_sq, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))
    num_components = n

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_i] = root_j
            return True
        return False

    for _, u, v in edges:
        if union(u, v):
            num_components -= 1
            if num_components == 1:
                return points[u][0] * points[v][0]

    return 0

real_input = "./Day_8/input.txt"

try:
    with open(real_input, 'r') as file:
        input_data = file.read()
    print(solve_playground_part2(input_data))
except FileNotFoundError:
    print(0)

# Answer : 6083499488 