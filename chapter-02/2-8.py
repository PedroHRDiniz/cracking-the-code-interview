# Given a circular linked list, implement an algorithm that returns the node at the beginning of the loop. DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node,
# so as to make a loop in the linked list.

import unittest


class Node:
    next = None

    def __init__(self, data):
        self.data = data


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    def set_child(self, node):
        parent = self.head
        while parent.next is not None:
            parent = parent.next
        parent.next = node


def return_loop_node(linked_list):
    hash_list = {}
    pointer = linked_list.head
    node = None
    while node is None:
        if hash(pointer) in hash_list:
            node = pointer
        else:
            hash_list[hash(pointer)] = True
            pointer = pointer.next

    return node


class Test(unittest.TestCase):
    def test_case_one(self):
        node_a = Node('a')
        node_b = Node('b')
        node_c = Node('c')
        node_d = Node('d')
        node_e = Node('e')
        linked_list = SinglyLinkedList(node_a)
        linked_list.set_child(node_b)
        linked_list.set_child(node_c)
        linked_list.set_child(node_d)
        linked_list.set_child(node_e)
        linked_list.set_child(node_c)
        self.assertEqual(linked_list.head.data, 'a')
        self.assertEqual(return_loop_node(linked_list).data, node_c.data)

    def test_case_two(self):
        node_a = Node('a')
        node_b = Node('b')
        node_c = Node('c')
        linked_list = SinglyLinkedList(node_a)
        linked_list.set_child(node_b)
        linked_list.set_child(node_c)
        linked_list.set_child(node_a)
        self.assertEqual(linked_list.head.data, 'a')
        self.assertEqual(return_loop_node(linked_list).data, node_a.data)


if __name__ == "__main__":
    unittest.main()
