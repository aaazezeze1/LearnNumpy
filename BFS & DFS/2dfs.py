# BFS and DFS both run in O(V + E) time complexity in general

import time
from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)  # Default dictionary to store graph

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function for DFS traversal
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recur for all adjacent nodes
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    # DFS function that initializes the traversal
    def DFS(self, start_node):
        visited = set()  # Use a set to track visited nodes
        self.DFSUtil(start_node, visited)

# Function to measure execution time for DFS
def measure_dfs(graph, start_node, scenario_name):
    start_time = time.time()  # Start time
    graph.DFS(start_node)
    end_time = time.time()  # End time
    print(f"\nExecution time for {scenario_name}: {end_time - start_time:.6f} seconds\n")

# Driver code to test DFS on different cases
if __name__ == '__main__':
    # Large Graph Test Case
    g = Graph()
    for i in range(9):  # Adding edges sequentially
        g.addEdge(i, i + 1)
    
    # g.DFS(0)  # Expected Output: 0 1 2 3 4 5 6 7 8 9
    measure_dfs(g, 0, "Large Graph Test Case")  # Expected Output: 0 1

    # Dense Graph Test Case
    g = Graph()
    nodes = 5
    for i in range(nodes):
        for j in range(nodes):
            if i != j:
                g.addEdge(i, j)

# g.DFS(0)  # Output varies based on recursion depth.
    measure_dfs(g, 0, "Dense Graph Test Case")  # Expected Output: 0 1

# Cyclic Graph Test Case
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)  # Cycle back to 0
g.addEdge(2, 3)
# g.DFS(0)  # Expected Output: 0 1 2 3 (without revisiting 0)
measure_dfs(g, 0, "Cyclic Graph Test Case")  # Expected Output: 0 1
