
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right








def rangeSumBST(root, L, R):
    ans = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if L <= node.val <= R:
                ans += node.val
            if L < node.val:
                stack.append(node.left)
            if node.val < R:
                stack.append(node.right)
    return ans

bst = TreeNode(10)
bst.left = TreeNode(5)
bst.right = TreeNode(15)
bst.left.left = TreeNode(3)
bst.left.right = TreeNode(7)
bst.right.right = TreeNode(18)

min = int(input("Enter the Lower value of the range : "))
max = int(input("Enter the Higher value of the range : "))

sol = rangeSumBST(bst, min, max)
print(f"The sum of the nodes in the range {min} and {max} is {sol}")