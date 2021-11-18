'''

task:

Implement the binary search algorithm

'''

import math 


def binary_search(array, target):
  min_index = 0
  max_index = (len(array) - 1)


  while(min_index <= max_index):
    p_index = math.floor(min_index + (max_index - min_index) / 2)
  
    if(array[p_index] == target):
      return p_index
    elif(array[p_index] < target):
      min_index = p_index + 1
    else:
      max_index = p_index - 1

  return -1

array = [0,1,21,33,45,45,61,71,72,73]
target = 33


array2 = [1,5,23,111]
target2 = 3


print(binary_search(array, target))
print(binary_search(array2, target2))
