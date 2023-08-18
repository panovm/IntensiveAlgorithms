from typing import Dict
from typing import List


# def depth_first_tree_traversal(root: int, tree: Dict[int, List[int]]) -> List[int]:
#     """
#     Completes depth first tree traversal and returns visited vertices
#     Go to left side of tree, then right, then self
# 
#     Args:
#         root (int): root vertex
#         tree (Dict[int, List[int]]): structure of tree
#                             (number of vertex, list of two elements: child number or None)
#     """
#     dict_visited = {k: 0 for k in tree.keys()}
# 
# 
#     return []


# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        tree_dict = {}

        def make_dict(r, parent=None):
            tree_dict[r.val] = [r.left, r.right]
            if parent is not None:
                tree_dict[r.val].append(parent)
            for item in tree_dict[r.val]:
                if item is not None and item != parent:
                    make_dict(item, parent=r)

        make_dict(root)
        tree_vivsted = {k: 0 for k in tree_dict.keys()}

        def dfs(r, k) -> list:
            tree_vivsted[r] = 1
            result = []
            if k == 0:
                result.append(r)
            for neighbour in tree_dict[r]:
                if neighbour is not None and tree_vivsted[neighbour.val] == 0:
                    result += dfs(neighbour.val, k - 1)
            return result

        return dfs(target.val, k)
