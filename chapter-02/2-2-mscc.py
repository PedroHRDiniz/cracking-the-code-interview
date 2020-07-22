def returnKthToLast(linkedList, k):
  if k == 0:
    return None
  if k == 1:
    return linkedList
  node = linkedList.head
  for i in range(1,k):
    if node is None:
      return None
    #if i < k-1:
    node = node.next
  return SinglyLinkedList(node)

#Milena Carneiro