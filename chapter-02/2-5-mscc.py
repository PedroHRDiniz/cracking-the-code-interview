#Non optimized version
#int and string can be out of bounds for too high values
#Redo it using mod operator 

#sum list in forward order
def concatAsString(list):
  head = list.head
  output = str(head.data)
  next = head.next
  while next is not None:
    output += str(next.data)
    next = next.next
  return output

def sumListsForwardOrder(list1, list2):
  list1AsNumber = int(concatAsString(list1))
  list2AsNumber = int(concatAsString(list2))
  sumLists = list1AsNumber + list2AsNumber
  sumAsString = str(sumLists)
  output = None
  index = 0
  for char in sumAsString:
    node = Node(char)
    if index == 0:
      output = SinglyLinkedList(node)
    else:
      output.setChild(node)
    index = index + 1
  return output

#sum list in reverse order
def numberFromList(list):
  unity = 10
  head = list.head
  output = head.data
  next = head.next
  while next is not None:
    multiplied = next.data * unity
    output = output + multiplied
    unity = unity * 10
    next = next.next
  return output

def sumListsReverseOrder(list1, list2):
  number1 = numberFromList(list1)
  number2= numberFromList(list2)
  sumLists = number1 + number2
  sumAsString = str(sumLists)
  output = None
  index = 0
  for char in sumAsString:
    node = Node(char)
    if index == 0:
      output = SinglyLinkedList(node)
    else:
      output.setChild(node)
    index = index + 1
  return output

#Milena Carneiro