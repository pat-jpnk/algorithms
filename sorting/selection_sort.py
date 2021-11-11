'''

task:

Implement the selection sort algorithm


Selection sort works by selecting a start-index, starting with the first and incrementing by one for each iteration. We are not iterating the start-index,
it stays the same during an iteration, increasing by one in-between iterations. This start-index is the same as our swap-index at the beginning of each iteration.
During the iteration, we move from the initial swap-index to the very end of the array, comparing the current swap-index to each index until the end. If during a comparison 
the newly hit index element is smaller than the current swap index, the element at the new index becomes the swap-index for that
iteration. Once the iteration is complete, we swap the start-index with the swap-index (if they are different).

'''

array = [8, 5, 2, 9, 5, 6, 3]


def selection_sort(array):
  focus_element = 0
  length = len(array)

  while(focus_element < length - 1):
    smallest_index = focus_element
    for i in range(focus_element + 1, length):
      if(array[smallest_index] > array[i]):
        smallest_index = i
    array[focus_element], array[smallest_index] = array[smallest_index], array[focus_element]
    focus_element += 1 


  return array


print(selection_sort(array))
