class Queue:
    def __init__(self):
        self.queue = list()

    def add_element(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        return False
    
    def size (self):
        return len(self.queue)
    
    def remove_element(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue")
    
TheQueue = Queue()
TheQueue.add_element("Apple")
TheQueue.add_element("Mango")
TheQueue.add_element("Guava")
TheQueue.add_element("Papaya")

print("The length of Queue", TheQueue)

print(TheQueue.remove_element())
print(TheQueue.remove_element())