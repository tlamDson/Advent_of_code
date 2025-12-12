import sys

# Increase recursion depth for deep graphs
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
            
    # Solve for paths from 'you' to 'out'
    return count_paths('you', adj, {})

def count_paths(node, adj, memo):
    # Base Case: Reached the target
    if node == 'out':
        return 1
    
    # Check memoization table
    if node in memo:
        return memo[node]
    
    # Dead end check
    if node not in adj:
        return 0
        
    total_paths = 0
    for neighbor in adj[node]:
        total_paths += count_paths(neighbor, adj, memo)
        
    # Store result
    memo[node] = total_paths
    return total_paths

# Assuming the file structure matches your previous example
with open("./Day_11/input.txt", 'r') as file:
    input_data = file.read()
print(f"Answer: {solve_reactor(input_data)}")

# Answer : (Depends on your specific input file)