"""
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). 
The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
"""

def has_path(edges, node_A, node_B):
  graph = build_graph(edges)
  return exists_path(graph, node_A, node_B, set())

def build_graph(edges):
  graph = {}
  
  for edge in edges:
    a, b = edge
    
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
      
    graph[a].append(b)
    graph[b].append(a)
    
  return graph
    
def exists_path(graph, src, dst, visited):
  if src == dst:
    return True
  
  if src in visited:
    return False
  
  visited.add(src)
  
  for neighbor in graph[src]:
    if exists_path(graph, neighbor, dst, visited) == True:
      return True
    
  return False