# Между этим классом и классом из предыдущей задачи есть несколько отличий, которые я помечу "!!!", 
# но изменения незначительны, так как изменения состоят лишь в том, что в прошлой задаче элементами кучи были массивы, а тут - числа

class MinHeap():  # Мин-куча - массив, где под индексом 0 - корень дерева, под индексами 2i+1 - левый потомок, 2i+2 - правый потомок
    def __init__(self):
        self.val = []

    def push(self, val = 0):    # !!!
        self.val.append(val)
        # Просеивание вверх
        i = len(self.val) - 1
        while i > 0:
            j = (i - 1) // 2
            if self.val[i] < self.val[j]:    # !!!
                t = self.val[j]
                self.val[j] = self.val[i]
                self.val[i] = t
                i = j
            else:
                break
        return None

    def pop(self):
        root = self.val[0]
        self.val[0] = self.val[-1]
        self.val.pop(-1)
        # Просеивание вниз
        n = len(self.val)
        node_ind = 0
        ind_swap = 0
        flag = 0   # Нужно ли менять узлы 
        while 1:
            left = 2 * node_ind + 1
            right = 2 * node_ind + 2
            if (left < n) and (self.val[left] < self.val[ind_swap]):    # !!!
                ind_swap = left
                flag = 1
            if (right < n) and (self.val[right] < self.val[ind_swap]):  # !!!
                ind_swap = right
                flag = 1
            if flag:
                t = self.val[ind_swap]
                self.val[ind_swap] = self.val[node_ind]
                self.val[node_ind] = t
                node_ind = ind_swap
                flag = 0
            else:
                break
        return root
    
# Реализовал поиск k-го наименьшего элемента через мин-кучу

def find_k_min(arr, k):
    minheap = MinHeap()
    for i in range(len(arr)):  # Инициализация мин-кучи
        minheap.push(arr[i])
    for i in range(k - 1):
        minheap.pop()
    return minheap.val[0]

# Инициализация кучи - N * log N
# Удаление К элементов из кучи - (K-1) * log N
# Итоговая сложность: (K-1 + N) * log N, где K - номер К-го минимального элемента, N - кол-во элементов в массиве
