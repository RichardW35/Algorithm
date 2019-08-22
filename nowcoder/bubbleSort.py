

def bubbleSort(arr):
          n = len(arr)
          if arr == None or n < 2 :
                    return 
          for i in range(n-1, 0, -1):
                    for j in range(i):
                              if arr[j] > arr[j+1]:
                                        arr[j], arr[j+1] = arr[j+1], arr[j]


 

arr = [3,4,1,5,3]
bubbleSort(arr)
print(arr)