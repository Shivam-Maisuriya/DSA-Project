 # Practical 6: Implementation of Binary Search Trees.
# Name: Shivam Maisuriya
# Enrollment No: 202203103510303
# Batch:B.Tech CSE

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def build_bst():
    root = None
    while True:
        data = input("Enter data to insert into the BST (or 'done' to finish): ")
        if data.lower() == 'done':
            break
        try:
            data = int(data)
            root = insert(root, data)
        except ValueError:
            print("Invalid input. Please enter an integer or 'done' to finish.")
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Main function
if __name__ == "__main__":
    print("Enter integers to build a binary search tree. Enter 'done' when finished.")
    bst_root = build_bst()

    print("\nInorder Traversal of Binary Search Tree:")
    inorder_traversal(bst_root)
