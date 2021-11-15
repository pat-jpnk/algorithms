'''

task:

Implement the heap sort algorithm


heapsort is not a 'stable' sorting algorithm

'''

import heapq 


array = [8, 5, 2, 9, 5, 6, 3]


# using python heapq module

def heap_sort_one(array):
  res = []
  for val in array:
    heapq.heappush(res, val)
  res = [heapq.heappop(res) for i in range(len(res))]
 
  
  return res


print(heap_sort_one(array))
