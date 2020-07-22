import math

class Node:
  next = None
  def __init__(self,data):
    self.data = data
    

class SinglyLinkedList:
  def __init__(self,head):
    self.head = head
    self.length = 1

  def setChild(self, node):
    parent = self.head
    while parent.next is not None:
      parent = parent.next
    parent.next = node
    self.length = self.length + 1

def isPalindrome(linkedList):
  if linkedList.length < 2: 
    return True
  else:
    counter = 0
    stackChars = []
    halfLength = math.floor(linkedList.length / 2)
    node = linkedList.head
    while counter < halfLength:
      stackChars.append(node.data)
      counter += 1
      node = node.next
    counter = counter - 1
    if linkedList.length % 2 == 1:
      node = node.next
    while node is not None and counter > -1:
      data = node.data
      currentChar = stackChars[counter]
      if data is not currentChar:
        return False
      stackChars.pop()
      counter = counter - 1
      node = node.next
  return True

#Milena Carneiro