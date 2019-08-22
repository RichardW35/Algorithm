def heapfy(arr, index, heapsize):
    left = index * 2 + 1
    while (left < heapsize):
        largest = left + 1 if (arr[left + 1] > arr[left + 1]
                               and left + 1 < heapsize) else left
        largest = largest if (arr[largest] > arr[index]) else index
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1


def heapInsert(arr, index):
    while (arr[index] > arr[int((index - 1) / 2)]):
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def heapSort(arr):
    length = len(arr)
    if arr == None or length < 2:
        return
    for i in range(length):
        heapInsert(arr, i)
    print(arr)
    swap(arr, 0, length - 1)
    length = length - 1
    while (length > 0):
        heapfy(arr, 0, length)
        swap(arr, 0, length - 1)
        length = length - 1


arr = [1, 5, 4, 6, 2, 7]

heapSort(arr)
print(arr)
