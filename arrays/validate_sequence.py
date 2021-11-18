'''

task: 

Given two non-empty arrays of integers, write a
function that determines whether the second
array is a subsequence of the first one.

A subsequence of an array is a set of numbers
that aren't necessarily adjacent in the array but
that are in the same order as they appear in the
array. 

For instance, the numbers [1, 3, 4]
form a subsequence of the array
[1, 2, 3, 4] , and so do the numbers
[2, 4]. 

Note that a single number in an
array and the array itself are both valid
subsequences of the array.

'''


def validate_subsequence(array, subsequence):
  arr_index = 0
  seq_index = 0
  arr_len = len(array)
  seq_len = len(subsequence)

  while(arr_index < arr_len):
    if(array[arr_index] == subsequence[seq_index]):
      seq_index += 1
      if(seq_index > (seq_len - 1)):
        return True
    
    arr_index += 1

  return False





array = [5,1,22,25,6,-1,8,19]
subsequence = [1,6,-1,10]

array2 = [5,1,22,25,6,-1,8,10]
subsequence2 = [5,1,22,25,6,-1,8,10]

print(validate_subsequence(array, subsequence))
print(validate_subsequence(array2, subsequence2))
