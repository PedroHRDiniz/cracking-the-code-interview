array_order_build = []
disc_dect_loop = {}
left_nodes = {}

class GraphNode:
    
    def __init__(self, data):
        self.data = data
        self.array_dependencia = []

    def set_child(self, node):
        self.array_dependencia.append(node)

def funcRecursivo(node):
    global disc_dect_loop
    global left_nodes
    if disc_dect_loop.get(node.data) is not None:
        raise Exception('deu ruim')
    disc_dect_loop[node.data] = True
    if node.data in array_order_build:
        return []
    if len(node.array_dependencia) <= 0:
        del left_nodes[node.data]
        del disc_dect_loop[node.data]
        return [node.data]
    internalArray = []
    for d in node.array_dependencia:
        internalArray += funcRecursivo(d)
    del left_nodes[node.data]
    del disc_dect_loop[node.data]
    return internalArray + [node.data]

def func(projects, dependencies):
    global left_nodes
    for p in projects:
        left_nodes[p] = GraphNode(p)
    for d in dependencies:
        left_nodes[d[1]].set_child(left_nodes[d[0]])
    
    while len(left_nodes) > 0 :
        key = list(left_nodes.keys())[0];
        temp = funcRecursivo(left_nodes.get(key))
        global array_order_build
        array_order_build += temp

    return array_order_build


# result = func(['A', 'B', 'C', 'D', 'E', 'F'], [['A', 'D'], ['F', 'B'], ['B', 'D'], ['F', 'A'], ['D', 'C']])
result2 = func(['A', 'B', 'C', 'D', 'E', 'F', 'G'], [['B', 'A'], ['G', 'A'], ['C', 'A'], ['D', 'C'], ['D', 'F'], ['F', 'G'], ['G', 'F']])

# print(result)
print(result2)
