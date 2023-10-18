import random

class BinarySearchTree:
    def __init__(self, value, depth=0):
        self.value = value
        self.depth = 0
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
            else:
                self.right.insert(value)

    def search(self, target):
        if self.value == target:
            return self
        elif target < self.value and self.left is not None:
            return self.left.search(target)
        elif self.right is not None:
            return self.right.search(target)
        else:
            return False

    def delete(self, value):
        pass


    def traversal(self):
        if self.left is not None:
            self.left.traversal()
        print(self.value)
        if self.right is not None:
            self.right.traversal()



def binary_search(arr, target): ## arr is sorted number list (from small to large)
    start = 0
    end = len(arr)
    if target < arr[0] or target > arr[-1]:
        return False
    while start < end:
        mid_index = (start + end) // 2
        mid_value = arr[mid_index]
        if target == mid_value:
            return mid_index
        if target < mid_value:
            end = mid_index
        if target > mid_value:
            start = mid_index + 1

    return False


# arr = [i for i in range(0, 20, 2)]
# print(arr)
# res = binary_search(arr, 15)
# print(res)

root = BinarySearchTree(50)
for i in range(0, 20):
    root.insert(random.randint(0,100))
root.traversal()
print(root.search(53))




