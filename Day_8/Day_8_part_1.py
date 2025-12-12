import re

def solve_playground(input_data):
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    points = []
    
    for line in lines:
        parts = list(map(int, line.split(',')))
        points.append(tuple(parts))

    n = len(points)
    if n == 0:
        return "Error: Empty input."

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist_sq = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist_sq, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))

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

    limit = 1000
    for k in range(min(len(edges), limit)):
        _, u, v = edges[k]
        union(u, v)

    circuit_sizes = {}
    for i in range(n):
        root = find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    sorted_sizes = sorted(circuit_sizes.values(), reverse=True)

    if len(sorted_sizes) < 3:
        return "Error: Less than 3 circuits found."

    return sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2]

real_input = "./Day_8/input.txt"

try:
    with open(real_input, 'r') as file:
        input_data = file.read()
    print(solve_playground(input_data))
except FileNotFoundError:
    print(0)

# Answer : 90036