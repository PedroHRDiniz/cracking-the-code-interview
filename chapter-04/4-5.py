class GraphNode:
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node


def validateBST(node):
    payloadBST = {
        'isBST': True,
        'min': node.data,
        'max': node.data
    }
    payloadBSTLeft = None
    payloadBSTRight = None
    if node.left is not None:
        payloadBSTLeft = validateBST(node.left)
    if node.right is not None:
        payloadBSTRight = validateBST(node.right)

    if payloadBSTLeft is not None:
        if not payloadBSTLeft['isBST'] or payloadBSTLeft['max'] > node.data:
            payloadBST['isBST'] = False
            return payloadBST
        else:
            payloadBST['min'] = payloadBSTLeft['min']
    if payloadBSTRight is not None:
        if not payloadBSTRight['isBST'] or payloadBSTRight['min'] <= node.data:
            payloadBST['isBST'] = False
            return payloadBST
        else:
            payloadBST['max'] = payloadBSTRight['max']

    return payloadBST


nodeA = GraphNode(20)
nodeB = GraphNode(0)
nodeC = GraphNode(30)
nodeD = GraphNode(10)
nodeE = GraphNode(12)
nodeF = GraphNode(1)
nodeG = GraphNode(25)

nodeA.setLeft(nodeF)
nodeA.setRight(nodeC)
nodeF.setLeft(nodeB)
nodeF.setRight(nodeD)
nodeD.setRight(nodeE)
nodeC.setLeft(nodeG)

print(validateBST(nodeA))
