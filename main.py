# import numpy as np

# # one dimensional array
# a = np.array([1, 2, 3])
# print(a)

# # 2d array of floats
# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# # get the dimension of the array https://youtu.be/QUT1VHiLmmI?si=phtSnpKYK5VQqKdM&t=788



import time
start_time = time.time()
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    
    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    
    # A function used by DFS
    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    
    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper function
        # to print DFS traversal
        self.DFSUtil(v, visited)


# Driver's code
if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2)")
    
    # Function call
    g.DFS(2)


print("\n--- %s seconds ---" % (time.time() - start_time))