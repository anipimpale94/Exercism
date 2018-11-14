class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)


class BinarySearchTree(object):
    def __init__(self, tree_data):
        self.root = None
        for item in tree_data:
            self.insert(item)

    def set_root(self, value):
        self.root = TreeNode(data=value)

    def insert(self, value):
        if self.root is None:
            self.set_root(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, current_node, value):
        if value <= current_node.data:
            if current_node.left:
                self.insert_node(current_node.left, value)
            else:
                current_node.left = TreeNode(data=value)
        elif value > current_node.data:
            if current_node.right:
                self.insert_node(current_node.right, value)
            else:
                current_node.right = TreeNode(value)

    def data(self):
        return self.root

    def sorted_data(self):
        return self.inorder(self.root, [])
    
    def inorder(self, currentNode, sorted_elements):
        if currentNode is not None:
            self.inorder(currentNode.left, sorted_elements)
            sorted_elements.append(currentNode.data)
            self.inorder(currentNode.right, sorted_elements)
        return sorted_elements