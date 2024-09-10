class Stack:
    def __init__(self):
        self.stack = []

    def add(self, data_val):
        if data_val not in self.stack:
            self.stack.append(data_val)
            return True
        else:
            return False
    
    def peek(self):
        return self.stack[-1]
    
    def remove(self):
        if len(self.stack) <= 0:
            return "No element in the stack"
        else:
            return self.stack.pop()
    
stack = Stack()
stack.add('Mon')
stack.add('Tue')
stack.add('Wed')
stack.add('Thu')
print(stack.peek())
print(stack.stack)