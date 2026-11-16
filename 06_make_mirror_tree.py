class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root):
    if root == None:
        return None
    t = root.right
    root.right = root.left
    root.left = t
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root

# Сложность: Мы меняем указатели у каждого узла дерева => линейная сложность 
# Зеркальное дерево - дерево, левые и правые поддеревья поменяны местами
# Это в программе и происходит: меняются местами указатели левых и правых поддеревьев всех узлов
