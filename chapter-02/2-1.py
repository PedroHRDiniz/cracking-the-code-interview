#classes and data structure for the exercise - Singly Linked List
class Node:
  next = None
  def __init__(self,data):
    self.data = data

class SinglyLinkedList:
  def __init__(self,head):
    self.head = head

  def setChild(self, node):
    parent = self.head
    while parent.next is not None:
      parent = parent.next
    parent.next = node

#2.1 Remove Duplicates (with additional buffer)
def removeDups(linkedList):
  buffer = {}
  parent = linkedList.head
  buffer[parent.data] = True
  
  pointer = parent.next
  while pointer is not None:
    character = pointer.data
    if character in buffer:
      parent.next = pointer.next
    else:
      buffer[character] = True
      parent = parent.next
    pointer = pointer.next
  return linkedList
