# class Solution:
#     arr = [1, 3, 2, 8, 4, 5, 7, 45, 9, 5, 6, 7]
#     Solution.reOrderArray(arr)
#     print(arr)

#     def reOrderArray(self, array):
#         n = len(array)
#         for i in range(1, n):
#             if array[i] % 2 == 1:
#                 for j in range(i - 1, 0, -1):
#                     if array[j] % 2 == 0:
#                         swap(array, j, j + 1)

#     def swap(self, arr, i, j):
#         tmp = arr[i]
#         arr[i] = arr[j]
#         arr[j] = tmp


def reOrderArray(array):
    n = len(array)
    for i in range(1, n):
        if array[i] % 2 == 1:
            for j in range(i - 1, 0, -1):
                if array[j] % 2 == 0:
                    swap(array, j, j + 1)


def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [1, 3, 2, 8, 4, 5, 7, 45, 9, 5, 6, 7]

reOrderArray(arr)
print(arr)