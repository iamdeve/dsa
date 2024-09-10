class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insertion(self, val):
        if self.data is None:
            print(val, "Root node is created")
            self.data = val
        else:
            p = self
            n = Node()
            n.data = val
            while True:
                if p.data > val:
                    if p.left is None:
                        print(val, "Left node is created")
                        p.left = n
                        break
                    else:
                        p = p.left
                else:
                    if p.right is None:
                        print(val, "Right node is created")
                        p.right = n
                        break
                    else:
                        p = p.right

root = Node()
root.insertion(10)
root.insertion(5)
root.insertion(20)
root.insertion(30)
root.insertion(25)
root.insertion(2)
