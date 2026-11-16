class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def find_k_min_elem(root, k, cnt):
    if root == None:
        return None
    left_res = find_k_min_elem(root.left, k, cnt)
    if left_res != None:
        return left_res
    cnt += 1
    if cnt == k:
        return root.val
    return find_k_min_elem(root.right, k, cnt)

# Использую обход в глубину (DFS)
