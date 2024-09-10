class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def search(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + " Not Found"
            return self.left.search(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + " Not Found"
            return self.right.search(val)
        else:
            print(str(self.data) + ' is found')

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

root = Node(27)

root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)

print(root.search(7))
print(root.search(14))
root.print_tree()