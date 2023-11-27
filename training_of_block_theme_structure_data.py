from binirytree import Node
root = Node(23)
root.left = Node(14)
root.right = Node( 30)
root.left.left = Node(7)
root.left.right = Node(16)
root.right.left = Node(24)
root.right.right = Node(40)
print(root)
def prerecord(node):
    if node is not None:
        print(node.value)
        prerecord(node.left)
        prerecord(node.right)
print("Обход дерева в прямом порядке")
prerecord(root)
def search(node,value):
    if node is None or value == node.value:
        return node
    if value < node.value:
        return search(node.left,value)
    return search(node.right,value)
print("Поиск элемента 14")
result = search(root,14)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")