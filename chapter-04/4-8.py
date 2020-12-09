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

def findNodes(ref, node1, node2):
  if ref is None:
    return 0
  elif ref is node1 or ref is node2:
    return 1 + findNodes(ref.left, node1, node2) + findNodes(ref.right, node1, node2)
  else:
    countChildrenLeft = findNodes(ref.left, node1, node2)
    countChildrenRight = findNodes(ref.right, node1, node2)
    if countChildrenLeft is -1 or countChildrenRight is -1:
      return -1
    totalChildren = countChildrenLeft + countChildrenRight
    if totalChildren is 2:
      print(ref.data)
      return -1
    else:
      return totalChildren

def firstCommonAncestor(root, node1, node2):
  if node1 is root or node2 is root:
    return None
  else:
    findNodes(root, node1, node2)

#exemplo
nodeA = GraphNode(20)
nodeB = GraphNode(8)
nodeC = GraphNode(22)
nodeD = GraphNode(4)
nodeE = GraphNode(12)
nodeF = GraphNode(10)
nodeG = GraphNode(14)

binaryTree = Graph(nodeA)
nodeA.setLeft(nodeB)
nodeA.setRight(nodeC)
nodeB.setLeft(nodeD)
nodeB.setRight(nodeE)
nodeE.setRight(nodeG)
nodeE.setLeft(nodeF)

firstCommonAncestor(nodeA, nodeF, nodeD)