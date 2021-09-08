from collections import deque

def traversal(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values

def has_path(graph, src, dst):  
  """
  n = number of nodes
  e = number edges
  Time: O(e)
  Space: O(n)
  """
  queue = deque([ src ])
  
  while queue:
    current = queue.popleft()
    
    if current == dst:
      return True
    
    for neighbor in graph[current]:
      queue.append(neighbor)
    
  return False

