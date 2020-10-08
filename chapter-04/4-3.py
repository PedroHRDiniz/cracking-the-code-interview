class GraphNode:
  left = None
  right = None
  def __init__(self,data):
    self.data = data

  def setLeft(self, node):
    self.left = node

  def setRight(self, node):
    self.right = node

class Graph:
  def __init__(self, root):
    self.root = root
    self.adjacencyDict = {
        self.root: []
    }

  def setEdge(node, vertex):
    if self.adjacencyDict[node] is None:
      self.adjacencyDict[node] = [];
    self.adjacencyDict[node].append(vertex)

dictLinkedList = {}
def addLinkedList(node, index):
  if node is None:
    return
  nodeLinkedList = Node(node.data)
  if index in dictLinkedList:
    depthLinkedList = dictLinkedList.get(index)
    depthLinkedList.setChild(nodeLinkedList)
    dictLinkedList.setdefault(index, depthLinkedList)
  else:
    newList = SinglyLinkedList(nodeLinkedList)
    dictLinkedList.setdefault(index, newList)
  addLinkedList(node.left, index + 1)
  addLinkedList(node.right, index + 1)

nodeA = GraphNode('A')
nodeB = GraphNode('B')
nodeC = GraphNode('C')
nodeD = GraphNode('D')
nodeE = GraphNode('E')
nodeF = GraphNode('F')
nodeG = GraphNode('G')
nodeH = GraphNode('H')
nodeI = GraphNode('I')

binaryTree = Graph(nodeA)
nodeA.setLeft(nodeB)
nodeA.setRight(nodeC)
nodeB.setLeft(nodeD)
nodeB.setRight(nodeE)
nodeC.setLeft(nodeF)
nodeC.setRight(nodeG)
nodeG.setRight(nodeH)
nodeH.setRight(nodeI)

addLinkedList(nodeA, 0)

def printLinkedList(linkedList):
  if linkedList is None:
    print('There\'s no linked list')
    return
  element = linkedList.head
  strList = ''
  while element is not None:
    strList += element.data + '-> '
    element = element.next
  print(strList)

for key in dictLinkedList.keys():
  printLinkedList(dictLinkedList[key])

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