class TreeNode():
    def __init__(self, val = 0, balance = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        self.balance = balance

def tree_balance_factor(root):
    if root == None:
        return 0
    left_h = tree_balance_factor(root.left)
    right_h = tree_balance_factor(root.right)
    root.balance = left_h - right_h
    return 1 + max(left_h, right_h)

# Высота вычисляется рекурсивно: доходим до листа, а потом идем наверх, прибавляя на каждом узле единицу
