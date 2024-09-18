def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

# Optimized bubble sort in Python

def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
        if not swapped:
            break

data = [-1, 43, 0, 13, -8]

bubbleSort(data)
print('Sorted Array in Ascending Order:')
print(data)
