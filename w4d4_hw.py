from bst import BinarySearchTree

from Node import Node

def make_bst(func):
    def wrapper(this_list):
        tree = BinarySearchTree(this_list[0])
        for ele in this_list[1:]:
            tree.add_node(ele)
        return func(tree)
    return wrapper

@make_bst
def treeify(someList):
    return(someList)

my_list = [1,4,55,6,10,2,33,30]

my_bst = treeify(my_list)

print(my_bst.get_min().value)

print(my_bst.get_max_while().value)