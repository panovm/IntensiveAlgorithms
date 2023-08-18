# from typing import Dict
# from typing import List


# def breadth_first_tree_traversal(root: int, tree: Dict[int, List[int]]) -> List[int]:
#     """
#     Completes breadth first tree traversal and returns visited vertices
#     Go to left side of tree, then right, then self

#     Args:
#         root (int): root vertex
#         tree (Dict[int, List[int]]): structure of tree
#                             (number of vertex, list of two elements: child number or None)
#     """

#     return []


# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = {}
        visited = {}
        queue = []
        def bfs(node_and_level):
            node, level = node_and_level
            if node is None:
                return False
            # if node.val not in result.get(level, []):
            result[level] = result.get(level, []) + [node.val]
            # visited[node.val] = 1
            for child in [node.left, node.right]:
                if child is not None and child.val not in visited.keys():
                    queue.append([child, level+1])
            if queue:
                next = queue.pop(0)
                if next[0]:
                    bfs(next)
        bfs((root, 0))

        result2 = []
        for i in range(len(result.keys())):
            result2.append(result[i])
        
        return result2

