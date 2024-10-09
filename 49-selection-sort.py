def selectionSort(array, size):
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]

size = len(data)

selectionSort(data, size)

print('Sorted array in ascending order')

print(data)

import sys

A = [64, 25, 12, 22, 11]

for i in range(len(A)):

    min_idx = i

    for j in range(i + 1, len(A)):

        if A[min_idx] > A[j]:

            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]

print("Sorted array in ascending order")

for i in range(len(A)):
    print("%d" % A[i], end =" ")

