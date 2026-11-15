def full_tree(root):
    if root == None:
        return True
    queue = [root]
    flag = False  # Видели ли мы пустой узел
    while len(queue) > 0:
        node = queue.pop(0)
        if node == None:
            flag = True
        else:
            if flag:
                return False
            queue.append(node.left)
            queue.append(node.right)
# Полное бинарное дерево - все уровни (кроме последнего) полностью заполнены, а на последнем уровне узлы заполняются слева направо
# Обход в ширину (BFS)
