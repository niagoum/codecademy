from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value  # data
        self.children = []  # references to other nodes

    def __repr__(self):
        return self.value

    def __str__(self):
        stack = deque()
        stack.append([self, 0])
        string = "\n"
        while len(stack) > 0:
            node, level = stack.pop()
            if level > 0:
                string += "|" * (level - 1) + "|-"
            string += str(node.value)
            string += "\n"
            level += 1 # 2
            for child in reversed(node.children): # n5
                stack.append([child, level])
        return string

    def add_child(self, child_node):
        # creates parent-child relationship
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        # removes parent-child relationship
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    ## breadth
    def print_all_value(self):
        q = deque()
        q.append(self)
        while q:
            node = q.pop()
            print(node.value)
            for i in node.children:
                q.append(i)
        return

    def get_all_value(self):
        q = deque()
        q.append(self)
        res = []
        while q:
            node = q.pop()
            res.append(node.value)
            for i in node.children:
                q.append(i)
        return res

    def print_path(self,depth=-1):
        q = deque()
        q.append([self, 0])
        while q:
            item = q.pop()
            print("|" * item[1] + "-" * (1 if item[1] else 0) + item[0].value)
            for i in item[0].children:
                q.append([i, item[1]+1])

    def get_path(self, depth=-1):
        arr_all_node = []
        arr = [[self]]
        arr_all_node += arr
        while depth:
            depth -= 1
            arr_t = []
            for i in arr:
                for j in i[-1].children:
                    k = i[:]
                    k.append(j)
                    arr_t.append(k)
            arr_all_node += arr_t
            if not arr_t or depth == 0:
                break
            arr = arr_t
        arr_all_value = []
        for i in arr_all_node:
            i_value = [j.value for j in i]
            arr_all_value.append(i_value)
        return arr_all_value

    def search_return_bool(self, goal, depth=-1):
        if self.value == goal:
            return True
        arr = [self]
        while depth:
            depth -= 1
            arr_t = []
            for i in arr:
                for j in i.children:
                    if j.value == goal:
                        return True
                    arr_t.append(j)
            if not arr_t:
                break
            arr = arr_t
        return False

    def search_return_path(self, goal, depth=-1):
        arr = [[self]]
        if self.value == goal:
            return arr
        while depth:
            depth -= 1
            arr_t = []
            for i in arr:
                for j in i[-1].children:
                    if j.value == goal:
                        return [k.value for k in i] + [j.value]
                    k = i[:]
                    k.append(j)
                    arr_t.append(k)
            if not arr_t:
                break
            if depth == 0:
                return False
            arr = arr_t
        return False

    ## depth
    def print_all_value_r(self):
        print(self.value)
        for i in self.children:
            i.print_all_value_r()

    def print_all_path_r(self, path = None):
        if path is None:
            path = [self.value]
        print(path)
        for i in self.children:
            path.append(i.value)
            i.print_all_path_r(path)
            path.pop()

    def get_all_value_r(self, arr=[]):
        arr.append(self.value)
        for i in self.children:
            i.get_all_value_r()
        return arr

    def get_all_path_r(self, path = None, arr = []):
        if path is None:
            path = [self.value]
        arr.append(path[:])
        for i in self.children:
            path.append(i.value)
            i.get_all_path_r(path)
            path.pop()
        return arr

    def search_r_return_bool(self, goal):
        if self.value == goal:
            return True
        for i in self.children:
            if i.search_r_return_bool(goal):
                return True
        return False

    def search_r_return_first_path(self, goal, path=None):
        if path is None:
            path = [self.value]
        if self.value == goal:
            return tuple(path)
        for i in self.children:
            path.append(i.value)
            path_find = i.search_r_return_first_path(goal, path)
            if path_find:
                return path_find
            path.pop()
        return None

    def search_r_return_all_path(self, goal, path=None, arr=[]):
        if path is None:
            path = [self.value]
        if self.value == goal:
            arr.append(path[:])
        for i in self.children:
            path.append(i.value)
            i.search_r_return_all_path(goal, path)
            path.pop()
        return arr


