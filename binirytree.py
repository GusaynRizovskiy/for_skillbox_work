from binarytree import Node
root = Node(10)
root.left = Node(8)
root.right = Node(12)
root.left.left = Node(5)
root.left.right = Node(9)
print("Структура бинарного дерева: ")
print(root)
# Обход дерева в прямом порядке (preorder)
def preorder(node):
    if node is not None:
        print(node.value)
        preorder(node.left)
        preorder(node.right)
print("Обход дерева в прямом порядке (preorder):")
preorder(root)
def search(node,value):
    if node is None or value == node.value:
        return node
    if value < node.value:
        return search(node.left, value)
    return search(node.right,value)
print("Поиск элемента в дереве:")
result = search(root, 9)
if result is not None:
    print("Элемент найден!")
else:
    print("Элемент не найден!")