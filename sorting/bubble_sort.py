'''
task: 

Implement the bubblesort algorithm


Bubble sort works by iterating through the array, in pairs of two adjacent elements, switching the 'left' and 'right'
element if [ 'left' > 'right' ], always decreasing the range of iteration by 1, per iteration, such that the biggest 
element 'bubbles' to the right end, during every iteration. The best time-complexity can be optimized by terminating 
the algorithm once there has been an iteration where no switches were made - meaning that the array is already sorted. 

'''

array = [8, 5, 2, 9, 5, 6, 3]

def bubble_sort(array):
	k = len(array)
	
	for i in range(0,k-1):
		flag = True
		for j in range(0,k-1-i):
			if(array[j] > array[j+1]):
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
				flag = False
		
		if(flag == True):
			return array
		
	return array

print(bubble_sort(array))
