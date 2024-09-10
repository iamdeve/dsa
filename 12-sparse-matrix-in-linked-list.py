class Node:
    __slots__ = "row", "col", "data", "next"
    def __init__(self, row = 0, col = 0, data = 0, next = None):
        self.row = row
        self.col = col
        self.data = data
        self.next = next

class Sparse:
    def __init__(self):
        self.head = None
        self.temp = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def create_new_node(self, row, col, data):
        temp = Node(row, col, data, None)
        
        if self.is_empty():
            self.head = temp
        else:
            self.temp.next = temp
        
        self.temp = temp

        self.size += 1

    def print_list(self):
        temp = r = s = self.head

        print("row_position:", end="")

        while temp != None:
            print(temp.row, end=" ")
            temp = temp.next
        print()

        print("column_position:", end="")
        while r != None:
            print(r.col, end=" ")
            r = r.next
        print()
        print("value:", end="")

        while s != None:
            print(s.data, end=" ")
            s = s.next

        print()

if __name__ == "__main__":
    s = Sparse()

    sparseMatrix = [
        [0,0,3,0,4],
        [0,0,5,7,0],
        [0,0,0,0,0],
        [0,2,6,0,0]
    ]

    for i in range(len(sparseMatrix)):
        for j in range(len(sparseMatrix[i])):
            if sparseMatrix[i][j] != 0:
                s.create_new_node(i, j, sparseMatrix[i][j])


    s.print_list()