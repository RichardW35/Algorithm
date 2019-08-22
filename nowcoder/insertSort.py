def insertSort(arr):
          n = len(arr)
          if arr == None or n < 2:
                    return
          for i in range(1,n):
                    for j in range(i-1, 0, -1):
                              if arr[j] > arr[j+1]:
                                        swap(arr, j, j+1)
def swap(arr, i ,j):
          tmp = arr[i]
          arr[i] = arr[j]
          arr[j] = tmp


arr = [1,3,2,8,4,5,7,45,9,5,6,7]

insertSort(arr)
print(arr)