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

    # Function to perform BFS traversal
    def BFS(self, s):
        # Use a dictionary for visited tracking to handle non-continuous node labels
        visited = {node: False for node in self.graph}

        # Create a queue for BFS
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)  # Dequeue a vertex
            print(s, end=" ")

            for i in self.graph[s]:
                if i not in visited or not visited[i]:  # Ensure key exists
                    queue.append(i)
                    visited[i] = True

# Function to measure execution time for BFS
def measure_bfs(graph, start_node, scenario_name):
    start_time = time.time()  # Start time
    graph.BFS(start_node)
    end_time = time.time()  # End time
    print(f"\nExecution time for {scenario_name}: {end_time - start_time:.6f} seconds\n")

# Driver code to test BFS on different cases
if __name__ == '__main__':
    # Large Graph Test Case
    g = Graph()
    for i in range(9):  # Adding edges sequentially
        g.addEdge(i, i + 1)
    
    # g.BFS(0)  # Expected Output: 0 1 2 3 4 5 6 7 8 9

    measure_bfs(g, 0, "Large Graph Test Case")

    # Dense Graph Test Case
    g = Graph()
    nodes = 5
    for i in range(nodes):
        for j in range(nodes):
            if i != j:
                g.addEdge(i, j)

# g.BFS(0)  # Expected Output: 0 1 2 3 4 (in some order)
    measure_bfs(g, 0, "Dense Graph Test Case")

# Disconnected Graph Test Case
g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(3, 4)  # Separate component

# g.BFS(0)  # Expected Output: 0 1 2 (3 and 4 won't be reached)
measure_bfs(g, 0, "Disconnected Graph Test Case")
