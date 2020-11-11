import unittest


class GraphNode:
    left = None
    right = None
    parent = None

    def __init__(self, data):
        self.data = data

    def set_left(self, node):
        self.left = node
        node.set_parent(self)

    def set_right(self, node):
        self.right = node
        node.set_parent(self)

    def set_parent(self, node):
        self.parent = node


def get_min(node):
    if node is None:
        return None
    min_value = node
    cursor = node.left
    while cursor is not None:
        min_value = cursor
        cursor = cursor.left
    return min_value


def get_in_order_successor(node):
    if node is None:
        return None

    if node.right is not None:
        return get_min(node.right)

    if node.parent is None:
        return None

    if node.parent.left is node:
        return node.parent

    cursor = node.parent
    ancestral = cursor.parent

    while ancestral is not None and ancestral.right is cursor:
        ancestral = ancestral.parent
        cursor = cursor.parent

    return ancestral


nodeA = GraphNode(20)
nodeB = GraphNode(8)
nodeC = GraphNode(22)
nodeD = GraphNode(4)
nodeE = GraphNode(12)
nodeF = GraphNode(10)
nodeG = GraphNode(14)

nodeA.set_left(nodeB)
nodeA.set_right(nodeC)
nodeB.set_left(nodeD)
nodeB.set_right(nodeE)
nodeE.set_left(nodeF)
nodeE.set_right(nodeG)


class Test(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(20, get_in_order_successor(nodeG).data)

    def test_case_two(self):
        self.assertEqual(None, get_in_order_successor(nodeC))

    def test_case_three(self):
        self.assertEqual(22, get_in_order_successor(nodeA).data)


if __name__ == "__main__":
    unittest.main()
