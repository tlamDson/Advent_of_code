import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

def solve_reactor(input_data):
    lines = input_data.strip().split('\n')
    adj = {}
    
    # Parse the input into an adjacency list
    for line in lines:
        if not line.strip(): continue
        
        parts = line.split(': ')
        source = parts[0]
        
        if len(parts) > 1:
            destinations = parts[1].split(' ')
            adj[source] = destinations
        else:
            adj[source] = []

    # Helper to count paths between any two specific nodes
    def count_between(start, end):
        return dfs_count(start, end, adj, {})

    # Calculate paths for Sequence 1: svr -> dac -> fft -> out
    path_seq_1 = (count_between('svr', 'dac') * count_between('dac', 'fft') * count_between('fft', 'out'))
    
    # Calculate paths for Sequence 2: svr -> fft -> dac -> out
    path_seq_2 = (count_between('svr', 'fft') * count_between('fft', 'dac') * count_between('dac', 'out'))
    
    # Sum the two mutually exclusive sets of paths
    return path_seq_1 + path_seq_2

def dfs_count(node, target, adj, memo):
    # Base Case: Reached the specific target for this segment
    if node == target:
        return 1
    
    if node in memo:
        return memo[node]
    
    # If dead end or node doesn't exist in map
    if node not in adj:
        return 0
        
    total = 0
    for child in adj[node]:
        total += dfs_count(child, target, adj, memo)
        
    memo[node] = total
    return total

with open("./Day_11/input.txt", 'r') as file:
    input_data = file.read()
print(f"Answer: {solve_reactor(input_data)}")

# Answer : 490695961032000