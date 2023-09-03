"""
Largest Component
---

Write a function, largest_component, that takes in the adjacency list of an undirected graph. 
The function should return the size of the largest connected component in the graph.

depth first

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
"""

def get_size(graph):
  visited = set()
  
  largest = 0
  for node in graph:
    size = explore_size(graph, node, visited)
    if size > largest:
      largest = size
  
  return largest

def explore_size(graph, node, visited):
  if node in visited:
    return 0

  visited.add(node)

  return 1 + sum(
      explore_size(graph, neighbor, visited) for neighbor in graph[node])