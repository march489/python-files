class BinaryNode:
    def __init__(self, name):
        self._left = None
        self._right = None
        self._name = name

    def set_left(self, other):
        self._left = other
    
    def set_right(self, other):
        self._right = other

def binary_depth_first_print(tree: BinaryNode): # depth-first traversal
    print(tree._name)
    if tree._left:
        binary_depth_first_print(tree._left)
    if tree._right:
        binary_depth_first_print(tree._right)



def binary_breadth_first_print(tree: BinaryNode):    # breadth-first traversal
    queue = [tree]
    while queue:
        if queue[0]._left:
            queue.append(queue[0]._left)
        if queue[0]._right:
            queue.append(queue[0]._right)
        print(queue[0]._name)
        queue = queue[1:]



class Node:
    def __init__(self, name):
        self._children = []
        self._name = name

    def add_child(self, child):
        self._children.append(child)

    def get_children(self):
        return self._children

def depth_first_print(tree: Node):      # depth-first traversal
    print(tree._name)
    for child in tree._children:
        depth_first_print(child)

def breadth_first_print(tree: Node):    # breadth-first traversal
    queue = []
    tmp = [tree]
    while tmp:
        print([node._name for node in tmp])
        queue.extend([node._name for node in tmp])
        tmp2 = []
        for node in tmp:
            tmp2.extend(node._children)
        tmp = tmp2
    print(queue)


if __name__ == '__main__':
    node0 = Node('node0')
    node1 = Node('node1')
    node2 = Node('node2')
    node3 = Node('node3')
    node4 = Node('node4')
    node5 = Node('node5')
    node6 = Node('node6')
    node7 = Node('node7')

    node0.add_child(node1)
    node0.add_child(node4)
    node1.add_child(node2)
    node1.add_child(node3)
    node3.add_child(node7)
    node4.add_child(node5)
    node4.add_child(node6)

    breadth_first_print(node0)
