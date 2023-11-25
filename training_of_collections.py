from binirytree import Node
t = Node(23)
t.left = Node(9)
t.right = Node(28)
t.left.left = Node(4)
t.left.right = Node(13)
t.right.left = Node(24)
t.right.right = Node(30)
print(t)
def prerecoder(node):
    if node is not None:
        print(node.value)
        prerecoder(node.left)
        prerecoder(node.right)
print("Обход дерева в прямом порядке (preorder):")
prerecoder(t)
def search(node,value):
    if node is None or value == node.value:
        return node
    if value <= node.value:
        return search(node.left,value)
    return search(node.right,value)
print("Поиск элемента в дереве:")
result = search(t, 24)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")


