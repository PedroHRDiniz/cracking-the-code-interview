import math

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