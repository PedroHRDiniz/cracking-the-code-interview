# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a
# binary search tree with minimal height.

import unittest
import math


class Node:
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def insert_left(self, node_left):
        self.left = node_left

    def insert_right(self, node_right):
        self.right = node_right


class BinarySearchTree:
    root = None

    def __init__(self, array):
        self.root = self.create_tree(array)

    def create_tree(self, array):
        if len(array) == 0:
            return None
        if len(array) == 1:
            return Node(array[0])
        index = math.floor((len(array)-1) / 2)
        node_data = array[index]
        node_to_return = Node(node_data)
        node_to_return.insert_left(self.create_tree(array[:index]))
        node_to_return.insert_right(self.create_tree(array[index+1:]))
        return node_to_return


class Test(unittest.TestCase):
    def test_case_one(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        binary_tree = BinarySearchTree(array)
        self.assertEqual(5, binary_tree.root.data)
        self.assertEqual(2, binary_tree.root.left.data)
        self.assertEqual(8, binary_tree.root.right.data)

    def test_case_two(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        binary_tree = BinarySearchTree(array)
        self.assertEqual(6, binary_tree.root.data)
        self.assertEqual(3, binary_tree.root.left.data)
        self.assertEqual(9, binary_tree.root.right.data)


if __name__ == "__main__":
    unittest.main()
