'''

task:

Implement the heap sort algorithm


fyi: heapsort is not a 'stable' sorting algorithm

'''


# class to construct max_heap

class heaps:
  def __init__(self):
    self.data = []
    self.count = 0

  def max_heap(self, array):
    for i in array:
      self.insert(i)
      self.perculate((self.count - 1))
    return self.data
  
  def insert(self, val):
    self.data.append(val)
    self.count += 1

  def perculate(self,index):
    if(index == 0):
      return
    else:
      p_i = self.parent_index(index)
      if(self.data[p_i] < self.data[index]):
        self.data[p_i], self.data[index] = self.data[index], self.data[p_i]
        self.perculate(p_i)

  def parent_index(self,i):
    return ((i - 1) // 2)

# heapsort algorithm

def heap_sort(heap):
  end = (len(heap) - 1)
  
  while(end > 0):
    heap[end], heap[0] = heap[0], heap[end]
    end -= 1
    sift_down(heap,0,end)

def sift_down(heap, start, end):
  root = start 

  while(((2 * start) + 1) <= end):
    child = ((2 * start) + 1)
    swap = root 

    if(heap[swap] < heap[child]):
      swap = child

    if(((child + 1) <= end) and (heap[swap] < heap[child + 1])):
      swap = (child + 1)
     
    if(swap == root):
      return

    else:
      heap[root], heap[swap] = heap[swap], heap[root]
      swap = root


data2 = [4,6,5,1,4]
data = [4,6,12,53,1,3]
kk = heaps()
jj = kk.max_heap(data)


print(jj)
heap_sort(jj)
print(" -> ",jj)
