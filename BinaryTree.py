class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        return node

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._find_min(node.right).key
            node.right = self._delete_recursive(node.right, node.key)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def inorder_traversal(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.key, end=" ")
                _inorder(node.right)

        _inorder(self.root)
        print()

if __name__ == "__main__":
    tree = BinaryTree()

    keys = [50, 30, 70, 20, 40, 60, 80]

    for key in keys:
        tree.insert(key)

    print("Inorder Traversal:")
    tree.inorder_traversal()

    tree.delete(30)
    print("Inorder Traversal after deleting 30:")
    tree.inorder_traversal()

    