'''

task:

Implement insertion sort


Insertion sort works by creating a partition of the array that starts with the first index element and grows by one index 
after each iteration of the present partition. At the start of each new partition, the new element, on the very right of the 
partition, is compared to each of the elements of the partition to the left. Once a comparison results in the element on the 
right being bigger than the element on the left, the comparisons are stopped and the next element is added to the partition.
This way, the is a growing partition growing from left to right, in which the new element on the right moves to the left until 
the element to its left is smaller or equal to it. 


'''


array = [8, 5, 2, 9, 5, 6, 3]


def insertion_sort(array):
  partition_index = 0
  leng = len(array)

  if(leng < 2):
    return array

  for j in range(0,leng):
    flag = True
    ind = j
    while(flag and ind > 0):
      if(array[ind] < array[ind - 1]):
        array[ind], array[ind - 1] = array[ind - 1], array[ind]
        ind -= 1
      else:
        flag = False
      
  return array



def insertion_sort_TWO(array):
  length = len(array)

  if length >= 2:
    for k in range(1,length):
      complete = False
      i = k
      while(True):
        if (i >= 1 and array[i-1] > array[i]):
          j = array[i-1]
          array[i-1] = array[i]
          array[i] = j
          i -= 1
        else:
          break
    return array

  else:
    return array



print(insertion_sort(array))

print(insertion_sort_TWO(array))
