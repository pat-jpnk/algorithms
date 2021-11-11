'''
task:

You're given an array of integers and another array of three distinct integers. The first array is guaranteed to only contain integers that are in the second array, and the second array represents a desired order for the integers in the first array. For example, a second array of 

[x,y,z]

represents a desired order of 

[x,x,...,x,y,y,...,y,z,z,...,z]

in the second array. 

Write a function that sorts the first array according to the desired order 
in the second array.

condition:

The function should perform this in-place (i.e. it should mutate the input array), and it shouldn't use any auxiliary space (i.e. it should run with 
constant space O(1) space.

'''

order = [0,1,-1] 
array = [1,0,0,-1,-1,0,1,1]


def three_number_sort(array, order):
  leng = len(order)
  count = [0] * leng
  j = 0

  for i in range(0, leng):
    for x in array:
      if(x == order[i]):
        count[i] += 1
  
  for k in range(0, leng):
    for o in range(0, count[k]):
      array[j] = order[k]
      j += 1

  return array




# this solution respects the "in-place" condition

def three_number_sort_TWO(array, order):
  if(len(array) <= 1):
    return array

  setting_index = 0

  for i in order: 
    for k in range(0,len(array)):
      if(array[k] == i):
        array[setting_index], array[k] = array[k], array[setting_index]
        setting_index += 1

  return array


print(three_number_sort(array,order))
print(three_number_sort_TWO(array,order))
