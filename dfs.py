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
    # Nodes (V) = 2, Edges (E) = 1
# Time Complexity: O(1)

    print("Best case scenario:")
    g1 = Graph()
    g1.addEdge(0, 1)
    measure_dfs(g1, 0, "Best Case")  # Expected Output: 0 1

# Nodes (V) = 5, Edges (E) = 5
# Time Complexity: O(5 + 5) = O(10) = O(V + E)

    print("Average case scenario:")
    g2 = Graph()
    g2.addEdge(0, 1)
    g2.addEdge(0, 3)
    g2.addEdge(1, 2)
    g2.addEdge(1, 4)
    g2.addEdge(3, 4)
    measure_dfs(g2, 0, "Average Case")  # Example Output: 0 1 2 3 4

# Nodes (V) = 9, Edges (E) = 8
# Time Complexity: O(9 + 8) = O(17) = O(V + E)

    print("Worst case scenario:")
    g3 = Graph()
    g3.addEdge(0, 1)
    g3.addEdge(0, 2)
    g3.addEdge(0, 3)
    g3.addEdge(1, 4)
    g3.addEdge(1, 5)
    g3.addEdge(2, 6)
    g3.addEdge(3, 7)
    g3.addEdge(3, 8)
    measure_dfs(g3, 0, "Worst Case")  # Example Output: 0 1 4 5 2 6 3 7 8
