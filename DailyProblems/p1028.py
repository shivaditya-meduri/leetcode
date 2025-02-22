# Problem link : https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/?envType=daily-question&envId=2025-02-22
'''
Problem description:
We run a preorder depth-first search (DFS) on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.

If a node has only one child, that child is guaranteed to be the left child.

Given the output traversal of this traversal, recover the tree and return its root.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_stack(root):
    if root is None:
        return []
    stack = [root]
    seen = []
    while stack:
        nextNode = stack.pop()
        if nextNode not in seen:
            seen.append(nextNode)
            if nextNode.right is not None:
                stack.append(nextNode.right)
            if nextNode.left is not None:
                stack.append(nextNode.left)
    return [n.val for n in seen]
  
class Solution:
    def changeFormat(self, traversal):
        currDep = 0
        traversal2 = []
        for n in traversal.split("-"):
            if n!="":
                traversal2.append([currDep, int(n)])
                currDep = 1
            else:
                currDep += 1
        return traversal2
    def recover(self, trav):
        currNode = TreeNode(val=trav[0][1])
        currDep = trav[0][0]
        lTreeBeg, rTreeBeg = None, None
        for ind, (di, vi) in enumerate(trav):
            if di == currDep + 1:
                if lTreeBeg is None:
                    lTreeBeg = ind
                else:
                    rTreeBeg = ind
        if lTreeBeg:
            currNode.left = self.recover(trav[lTreeBeg:rTreeBeg])
        if rTreeBeg:
            currNode.right = self.recover(trav[rTreeBeg:])
        return currNode
            
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        traversal2 = self.changeFormat(traversal)
        root = self.recover(traversal2)
        return dfs_stack(root)

a = Solution()
tcs = ["1-2--3--4-5--6--7", "1-2--3---4-5--6---7", "1-401--349---90--88"]
for tc in tcs:
    print(a.recoverFromPreorder(tc))
