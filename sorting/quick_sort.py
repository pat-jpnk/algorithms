'''

task:

Implement quick sort



'''

array = [8, 5, 2, 9, 5, 6, 3]


def quick_sort(array):
  partition(array, 0, len(array) - 1)
  return array  

def partition(array, start_i, end_i):


  if(start_i >= end_i):
    return

  p = start_i
  l = start_i + 1
  r = end_i


  while(r >= l):
    if(array[l] > array[p] and array[r] < array[p]):
      array[l], array[r] = array[r], array[l]
    if(array[l] <= array[p]):
      l += 1 
      
    if(array[r] >= array[p]):
      r -= 1

  array[r], array[p] = array[p], array[r]
  
  leftSmaller = (r - 1 - start_i) < (end_i - (r + 1))
  
  if(leftSmaller):
    partition(array, start_i, r - 1)
    partition(array, r + 1, end_i)
  else:
    partition(array, r + 1, end_i)
    partition(array, start_i, r -1)




print(quick_sort(array))
