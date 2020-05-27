# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.
# EXAMPLE
# Input: the node c from the linked list a - >b- >c - >d - >e- >f
# Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
import unittest


class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def delete_middle_node(node):
    next = node.next
    node.data = next.data
    node.next = next.next


class Test(unittest.TestCase):
    def test_delete_middle_node(self):
        head = Node('a', Node('b', Node('c', Node('d'))))
        node_c = head.next.next
        delete_middle_node(node_c)
        print(node_c.data)
        self.assertEqual(head.data, 'a')
        self.assertEqual(head.next.data, 'b')
        self.assertEqual(head.next.next.data, 'd')


if __name__ == "__main__":
    unittest.main()