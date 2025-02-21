# Problem link : https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2025-02-21
'''
Problem description:
Given a binary tree with the following rules:

root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:

FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
'''
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

### Time efficient
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.elems = set()
        self.recover(self.root, 0)

    def recover(self, node, ind):
        node.val = ind
        self.elems.add(ind)
        if node.left:
            self.recover(node.left, 2*ind+1)
        if node.right:
            self.recover(node.right, 2*ind+2)

    def find(self, target: int) -> bool:
        if target in self.elems:
            return True
        else:
            return False

### Memory efficient
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.recover(self.root, 0)

    def recover(self, node, ind):
        node.val = ind
        if node.left:
            self.recover(node.left, 2*ind+1)
        if node.right:
            self.recover(node.right, 2*ind+2)

    def generate_moves(self, target, moves=None):
        if moves is None:
            moves = []
        if target == 0:
            return moves[::-1]
        if target%2==0:
            parent = (target-2)//2
            moves.append("R")
            return self.generate_moves(parent, moves)
        else:
            parent = (target-1)//2
            moves.append("L")
            return self.generate_moves(parent, moves)
    
    def find(self, target: int) -> bool:
        if target == 0:
            return True
        moves = self.generate_moves(target)
        curr = self.root
        for m in moves:
            if m == "L":
                if curr.left is None:
                    return False
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    return False
                else:
                    curr = curr.right
        return curr.val == target
            
