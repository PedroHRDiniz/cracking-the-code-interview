# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

import unittest


class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next


def find_kth_to_last(head, k):
    node = head
    follow = head
    for n in range(k):
        if not node:
            return None
        node = node.next
    while node:
        node = node.next
        follow = follow.next
    return follow


class Test(unittest.TestCase):
    def test_kth_to_last(self):
        head = Node('a', Node('b', Node('c', Node('d', Node('e', Node('f', Node('g')))))))
        self.assertEqual(None, find_kth_to_last(head, 0))
        self.assertEqual('g', find_kth_to_last(head, 1).data)
        self.assertEqual('c', find_kth_to_last(head, 5).data)
        self.assertEqual('a', find_kth_to_last(head, 7).data)
        self.assertEqual(None, find_kth_to_last(head, 8))


if __name__ == "__main__":
    unittest.main()