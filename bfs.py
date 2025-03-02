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
    # Nodes (V) = 2, Edges (E) = 1
# Time Complexity: O(2 + 1) = O(1)

    print("Best case scenario:")
    g1 = Graph()
    g1.addEdge(0, 1)
    measure_bfs(g1, 0, "Best Case")  # Expected Output: 0 1

# Nodes (V) = 5, Edges (E) = 5
# Time Complexity: O(5 + 5) = O(10) = O(V + E)

    print("Average case scenario:")
    g2 = Graph()
    g2.addEdge(0, 1)
    g2.addEdge(0, 3)
    g2.addEdge(1, 2)
    g2.addEdge(1, 4)
    g2.addEdge(3, 4)
    measure_bfs(g2, 0, "Average Case")  # Example Output: 0 1 3 2 4

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
    measure_bfs(g3, 0, "Worst Case")  # Example Output: 0 1 2 3 4 5 6 7 8
