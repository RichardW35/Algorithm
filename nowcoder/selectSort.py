def selectSort(arr):
          n = len(arr)
          if arr == None or n < 2:
                    return
          for i  in range(n-1):
                    minIndex = i
                    for j in range(i+1, n):
                              minIndex = j if (arr[j] < arr[minIndex]) else minIndex
                    swap(arr, i, minIndex)

def swap(arr, i ,j):
          tmp = arr[i]
          arr[i] = arr[j]
          arr[j] = tmp


arr = [1,3,2,8,3,5,7,3,2,5,6,7]

selectSort(arr)
print(arr)