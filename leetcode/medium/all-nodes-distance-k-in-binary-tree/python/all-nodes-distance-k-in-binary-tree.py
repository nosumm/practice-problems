# Solution for all-nodes-distance-k-in-binary-tree (Python)
# Problem: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK(root, target, k):
    parent = {}
    def build_parent(node, par):
        if node:
            parent[node] = par
            build_parent(node.left, node)
            build_parent(node.right, node)
    build_parent(root, None)

    queue = deque([(target, 0)])
    visited = set([target])
    result = []

    while queue:
        node, distance = queue.popleft()

        if distance == k:
            result.append(node.val)
            continue # stop exploring this node
        # explore left child
        if node.left and node.left not in visited:
            visited.add(node.left)
            queue.append((node.left, distance + 1))
        # explore right child
        if node.right and node.right not in visited:
            visited.add(node.right)
            queue.append((node.right, distance + 1))
        # explore parent
        par = parent[node]
        if par and par not in visited:
            visited.add(par)
            queue.append((par, distance + 1))
    return result




if __name__ == '__main__':
    # Example tree construction
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left  # Node with value 5
    k = 2
    print(distanceK(root, target, k))  # Output: [7, 4, 1]