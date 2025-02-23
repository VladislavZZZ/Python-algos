# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) > 0 and len(postorder) > 0:
            node_val = preorder.pop(0)
            postorder.pop()
            shift = 1 if len(postorder) > 0 else 0
            if not preorder:
                edge =shift
            else:
                edge = postorder.index(preorder[0]) + shift
            return TreeNode(node_val, self.constructFromPrePost(preorder=preorder[:edge], postorder=postorder[:edge]),
                            self.constructFromPrePost(preorder=preorder[edge:], postorder=postorder[edge:]))


if __name__ == '__main__':
    sol = Solution()
    pre = [1]
    post = [ 1]
    tree = sol.constructFromPrePost(pre, post)
    print("done")
