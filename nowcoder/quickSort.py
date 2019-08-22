def partition(arr, l, r):
          less = l - 1
          more = r
          while(l < more):
                    if arr[l] < arr[r]:
                              swap(arr, less+1, l)
                              l = l+1
                              less = less+1
                    elif arr[l] > arr[r]:
                              swap(arr, more-1, l)
                              more = more-1
                    else:
                              l = l+1
          swap(arr, more, r)
          return [less+1, more]
                              
def swap(arr, i ,j):
          tmp = arr[i]
          arr[i] = arr[j]
          arr[j] = tmp


def quickSort(arr):
          if arr == None or len(arr) < 2:
                    return []
          quick_Sort(arr, 0, len(arr)-1)

def quick_Sort(arr, l, r):
          if l < r:
                    p = partition(arr, l, r)
                    quick_Sort(arr, l, p[0] - 1)
                    quick_Sort(arr, p[1] + 1, r)

arr = [1,3,2,8,3,5,7,3,2,5,6,7]

quickSort(arr)

print(arr)