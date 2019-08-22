def mergeSort(arr):
          if arr == None or len(arr) < 2:
                    return arr
          mid  = len(arr)/2
          left = mergeSort(arr[:mid])
          right = mergeSort(arr[mid:])
          return merge(left,right)

def merge(a, b):
          c = []
          i = j = 0
          while i < len(a) and j < len(b):
                    if a[i] <= b[j]:
                              c.append(a[i])
                              i = i+1
                    else:
                              c.append(b[j])
                              j = j+1
          if i == len(a):
                    for h in b[j:]:
                              c.append(h)
          else:
                    for h in a[i:]:
                              c.append(h)
          return c
          

                    
          

arr = [1,3,2,8,3,5,7,3,2,5,6,7,10]

mergeSort(arr)
print(arr)