# 235 Lowest Common Ancestor of a Binary Search Tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return root.val
        if p.val < q.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > q.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
