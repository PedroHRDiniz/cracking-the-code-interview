#  Palindrome: Implement a function to check if a linked list is a palindrome.

import unittest
import math


class Node:
    next = None

    def __init__(self, data):
        self.data = data


class SinglyLinkedList:
    def __init__(self, head):
        self.head = head
        self.length = 1

    def set_child(self, node):
        parent = self.head
        while parent.next is not None:
            parent = parent.next
        parent.next = node
        self.length += 1


def is_palindrome(linked_list):
    half_length = math.floor(linked_list.length / 2)
    is_even = linked_list.length % 2 == 0
    stack = []
    pointer = linked_list.head
    for i in range(linked_list.length):
        if i < half_length:
            stack.append(pointer)
            pointer = pointer.next
            continue

        if not is_even and i == half_length:
            pointer = pointer.next
            continue

        node_to_compare = stack.pop()
        if node_to_compare.data != pointer.data:
            return False
        pointer = pointer.next

    return True


class Test(unittest.TestCase):
    def test_case_one(self):
        no_a = Node('b')
        no_b = Node('b')
        no_c = Node('a')
        no_d = Node('b')
        no_e = Node('c')
        linked_list = SinglyLinkedList(no_a)
        linked_list.set_child(no_b)
        linked_list.set_child(no_c)
        linked_list.set_child(no_d)
        linked_list.set_child(no_e)
        self.assertEqual(linked_list.length, 5)
        self.assertEqual(linked_list.head.data, 'b')
        self.assertEqual(is_palindrome(linked_list), False)

    def test_case_two(self):
        no_a = Node('b')
        no_b = Node('b')
        no_c = Node('a')
        no_d = Node('b')
        no_e = Node('b')
        linked_list = SinglyLinkedList(no_a)
        linked_list.set_child(no_b)
        linked_list.set_child(no_c)
        linked_list.set_child(no_d)
        linked_list.set_child(no_e)
        self.assertEqual(linked_list.length, 5)
        self.assertEqual(linked_list.head.data, 'b')
        self.assertEqual(is_palindrome(linked_list), True)

    def test_case_three(self):
        no_a = Node('b')
        no_b = Node('b')
        no_d = Node('b')
        no_e = Node('b')
        linked_list = SinglyLinkedList(no_a)
        linked_list.set_child(no_b)
        linked_list.set_child(no_d)
        linked_list.set_child(no_e)
        self.assertEqual(linked_list.length, 4)
        self.assertEqual(linked_list.head.data, 'b')
        self.assertEqual(is_palindrome(linked_list), True)

    def test_case_four(self):
        no_a = Node('b')
        no_b = Node('b')
        no_d = Node('b')
        no_e = Node('c')
        linked_list = SinglyLinkedList(no_a)
        linked_list.set_child(no_b)
        linked_list.set_child(no_d)
        linked_list.set_child(no_e)
        self.assertEqual(linked_list.length, 4)
        self.assertEqual(linked_list.head.data, 'b')
        self.assertEqual(is_palindrome(linked_list), False)


if __name__ == "__main__":
    unittest.main()

