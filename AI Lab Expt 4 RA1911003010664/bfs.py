from collections import deque
 
# Class for node of the Tree
class Node:
    def __init__(self,v):
        self.val = v
        self.left = None
        self.right = None
 
# Function to perform level order
# traversal on the Tree and
# calculate the required sum
def rangeSumBST(root, low, high):
    sum = 0
     
    # Base Case
    if (root == None):
        return 0
 
    # Stores the nodes while
    # performing level order traversal
    q = deque()
     
    # Push the root node
    # into the queue
    q.append(root)
 
    # Iterate until queue is empty
    while (len(q) > 0):
 
        # Stores the front
        # node of the queue
        curr = q.popleft()
        # q.pop()
 
        # If the value of the node
        # lies in the given range
        if (curr.val >= low
            and curr.val <= high):
 
            # Add it to sum
            sum += curr.val
 
        # If the left child is
        # not NULL and exceeds low
        if (curr.left != None
            and curr.val > low):
 
            # Insert into queue
            q.append(curr.left)
 
        # If the right child is not
        # NULL and exceeds low
        if (curr.right != None
            and curr.val < high):
 
            # Insert into queue
            q.append(curr.right)
 
    # Return the resultant sum
    return sum
 
# Function to insert a new node
# into the Binary Search Tree
def insert(node, data):
   
    # Base Case
    if (node == None):
        return Node(data)
 
    # If the data is less than the
    # value of the current node
    if (data <= node.val):
 
        # Recur for left subtree
        node.left = insert(node.left, data)
    # Otherwise
    else:
        # Recur for the right subtree
        node.right = insert(node.right, data)
 
    # Return the node
    return node
 
# Driver Code
if __name__ == '__main__':
    # /* Let us create following BST
    #      10
    #     / \
    #    5   15
    #   / \     \
    #  3   7    18  */
    root = None
    root = insert(root, 10)
    root = insert(root, 5)
    root = insert(root, 15)
    root = insert(root, 3)
    root = insert(root, 7)
    root = insert(root, 18)
 
   
    L = int(input("Enter the Lower value of the range : "))
    R = int(input("Enter the Higher value of the range : "))
    sol=rangeSumBST(root, L, R)
    print(f"The sum of the nodes in the range {L} and {R}  is {sol}")
