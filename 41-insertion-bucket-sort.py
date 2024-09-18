def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucketSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
    for i in range(slot_num):
        arr[i] = insertion_sort(arr[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x

x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Original Array:", x)
x = bucketSort(x)
print("Sorted Array:", x)
