"""
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph. 
The function should return the number of connected components within the graph.

depth first

n = number of nodes
e = number edges
Time: O(e)
Space: O(n)
"""

def count(graph):
  visited = set()
  count = 0
  
  for node in graph:
    if explore(graph, node, visited) == True:
      count += 1
      
  return count

def explore(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    explore(graph, neighbor, visited)
  
  return True