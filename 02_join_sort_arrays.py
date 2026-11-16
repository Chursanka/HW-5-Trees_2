class MinHeap():  # Мин-куча - массив, где под индексом 0 - корень дерева, под индексами 2i+1 - левый потомок, 2i+2 - правый потомок
    def __init__(self):
        self.val = []

    def push(self, val = []):
        self.val.append(val)
        # Просеивание вверх
        i = len(self.val) - 1
        while i > 0:
            j = (i - 1) // 2
            if self.val[i][0] < self.val[j][0]:
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
            if (left < n) and (self.val[left][0] < self.val[ind_swap][0]):
                ind_swap = left
                flag = 1
            if (right < n) and (self.val[right][0] < self.val[ind_swap][0]):
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




def join_sort_arrays(arr_of_arr):
    res = []
    minheap = MinHeap()
    for i in range(len(arr_of_arr)):
        cur_arr = arr_of_arr[i]
        if len(cur_arr) > 0:
            minheap.push([cur_arr[0], i, 0])
    while len(minheap.val) > 0:
        value, ind_arr, ind_elem = minheap.pop()
        res.append(value)
        if ind_elem + 1 < len(arr_of_arr[ind_arr]):
            next_elem = arr_of_arr[ind_arr][ind_elem + 1]
            minheap.push([next_elem, ind_arr, ind_elem + 1])
    return res

# K * log K - создание кучи (для каждого массива (их К штук) мы кладем элемент в кучу (за log K))
# N * 2log K - цикл (для каждого элемента в куче (их N) мы в худшем случае достаем из кучи и добавляе в кучу элемент (log K + log K))
# (K - кол-во массивов, N - число всех элементов массивов)
# Итоговая сложность: log K * (K + 2N)
