"""
Write a function, depth_first_values, that takes in the root of a binary tree. 
The function should return a list containing all values of the tree in depth-first order.
"""

def traversal_recursive(root):
    if not root:
        return []

    left_values = traversal_recursive(root.left)
    right_values = traversal_recursive(root.right)
    return [root.val, *left_values, *right_values]


def traversal_iterative(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


def has_path(graph, src, dst):
    """
    n = number of nodes
    e = number edges
    Time: O(e)
    Space: O(n)
    """
    if src == dst:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dst) == True:
            return True
    
    return False

