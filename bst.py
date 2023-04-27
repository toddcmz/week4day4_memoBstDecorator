from Node import Node

class BinarySearchTree:

    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, value, node=None): # this is the recursive solution
        if not node:
            node = self.root
        if value > node.value:
            if not node.right:
                node.right = Node(value)
                return
            else:
                return self.add_node(value, node.right)
        else:
            if not node.left:
                node.left = Node(value)
                return
            else:
                return self.add_node(value, node.left)
            
        

    def get_min(self, node=None):
        if not node:
            node=self.root
        if node.left:
            return self.get_min(node.left)
        else:
            return node


    def get_max_recurse(self, node=None):
        if not node:
            node=self.root
        if node.right:
            return self.get_min(node.right)
        else:
            return node
        
    def get_max_while(self):
        node = self.root
        while node.right:
            node=node.right
        return node


    def does_contain(self, target):
        node = self.root
        while node.value != target:
            if target > node.value:
                if node.right:
                    node = node.right
                else:
                    return False
            else:
                if node.left:
                    node=node.left
                else:
                    return False
        return True
    
    def print_in_order(self, node=None):
        if not node:
            node = self.root
        if node:
            if node.left:
                self.print_in_order(node.left)
            print(node.value)
            if node.right:
                self.print_in_order(node.right)
        
        

# bst = BinarySearchTree(100)
# bst.add_node(10)
# bst.add_node(130)
# bst.add_node(51)
# bst.add_node(80)
# bst.add_node(77)
# print(bst.root.left.value)

# bst.add_node(90)
# print(bst.root.left.right.value)

# bst.add_node(105)
# print(bst.root.right.value)

# print(bst.get_min().value)

# bst.add_node(30)
# print(bst.get_min().value)

# print(bst.get_max_recurse().value)
# print(bst.get_max_while().value)

# print(bst.does_contain(30))
# print(bst.does_contain(25))
# print(bst.does_contain(105))

# bst.print_in_order()
