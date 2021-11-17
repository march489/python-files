import random

class BinaryNode:
    def __init__(self, data: list):
        self._left = None
        self._right = None
        self._data = data

    def set_left(self, other):
        self._left = other
    
    def set_right(self, other):
        self._right = other

def split_list_items(ls: list):
    if len(ls) <= 1:
        pass
    else:
        mid = len(ls) // 2
        return[ls[:mid], ls[mid:]]

def merge_sort(ls):
    pass

def insertion_sort(ls):
    sorted_list = []
    while ls:
        tmp = ls.pop()
        index = 0
        for item in sorted_list:
            if item > tmp:
                break
            index += 1
        sorted_list.insert(index, tmp)
    return sorted_list

if __name__ == '__main__':
    print(insertion_sort([1, 7, 9, 11, 12, 4 ,0 ,9]))
    print(insertion_sort([random.randint(1,1000) for i in range(100)]))