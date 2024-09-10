class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class SLinkedList:
    def __init__(self):
        self.head_val = None

    def listprint(self):
        print_val = self.head_val
        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next_node

    def atBeginning(self, newData):
        newNode = Node(newData)
        newNode.next_node = self.head_val
        self.head_val = newNode
    
    def atEnd(self, newData):
        newNode = Node(newData)
        if self.head_val is None:
            self.head_val = newNode
            return
        last = self.head_val
        while(last.next_node):
            last = last.next_node
        last.next_node = newNode
    
    def inBetween(self, middle_node, newData):
        if middle_node is None:
            print("The mention node is absent")
            return
        newNode = Node(newData)
        newNode.next_node = middle_node.next_node
        middle_node.next_node = newNode
    
    def removeNode(self, removeKey):
        head_val = self.head_val
        if head_val is not None:
            if head_val.data == removeKey:
                self.head_val = head_val.next_node
                head_val = None
                return
        while head_val is not None:
            if head_val.data == removeKey:
                break
            prev = head_val
            head_val = head_val.next_node
        
        if head_val == None:
            return
        prev.next_node = head_val.next_node
        head_val = None

list = SLinkedList()
list.head_val = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list.head_val.next_node = e2
e2.next_node = e3

list.atBeginning('Sun')

list.atEnd('Thu')

list.inBetween(list.head_val.next_node, "Fri")

list.listprint()

list.removeNode('Fri')

list.listprint()