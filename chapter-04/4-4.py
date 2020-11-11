class GraphNode:
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node


def calcular_altura(node):
    obj = {
        'isBalanced': True,
        'altura': 0
    }
    altura_esq = 0
    altura_dir = 0
    if node is None:
        return
    if node.left is not None:
        altura_esq += 1
        obj_filho = calcular_altura(node.left)
        if not obj_filho['isBalanced']:
            obj['isBalanced'] = False
            return obj
        altura_esq += obj_filho['altura']
    if node.right is not None:
        altura_dir += 1
        obj_filho = calcular_altura(node.right)
        if not obj_filho['isBalanced']:
            obj['isBalanced'] = False
            return obj
        altura_dir += obj_filho['altura']
    if abs(altura_esq - altura_dir) > 1:
        obj['isBalanced'] = False
    obj['altura'] = max(altura_esq, altura_dir)
    return obj


nodeA = GraphNode('A')
nodeB = GraphNode('B')
nodeC = GraphNode('C')
nodeD = GraphNode('D')
nodeE = GraphNode('E')
nodeF = GraphNode('F')
nodeG = GraphNode('G')
nodeH = GraphNode('H')
nodeI = GraphNode('I')

print(calcular_altura(nodeA))
