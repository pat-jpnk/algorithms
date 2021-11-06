'''

task: 

Write a function that finds an integer 'x' in an unsorted array 'A'
and returns the index of the element's first occurence
if it is contained in the arra, ootherwise return -1.

'''

A = [3,7,5,1,0,9,4,2,13]

x = 4


def linear_sort(x,A):
  for i in range(0,len(A)):
    if(A[i] == x):
      return i
  return -1


print(linear_sort(x,A))


'''

linear sort 

O(n)


'''
