'''

task:

Implement the heap sort algorithm


heapsort is not a 'stable' sorting algorithm

'''


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
'''


# range(start, stop, step)


'''

       (0)
     /    \
   (1)    (2)
  /  \    /  \
 (3) (4) (5) (6)


Treap key structure

in array: [0,1,2,3,4,5,6]

'''

data = [4,6,12,53,1,3]
data5 = [4,6,12,53,1]

data2 = [2,1]
data3 = [63,23,51,341,32,11]
data4 = [4,35,231,12,33,2,24,21,6,3,8,3,93,1,92,19,15,13,7,13,6,21,17]

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
      #print("p_i _ index: ", p_i, index)
      if(self.data[p_i] < self.data[index]):
        self.data[p_i], self.data[index] = self.data[index], self.data[p_i]
        self.perculate(p_i)

  def parent_index(self,i):
    return ((i - 1) // 2)

jj = heaps()

kk = heaps()

#print(jj.max_heap(data))
#print(kk.max_heap(data5))
#print(jj.max_heap(data2))
#print(jj.max_heap(data3))
#print(jj.max_heap(data4))





'''
def heap_sort(data):
  k = heaps()
    j = k.max_heap(data)
  end_index = (len(j) - 1)

  while(end_index > 1):
    j[0], j[end_index] = j[end_index], j[0]
    end_index -= 1
#    print(len(j) - 1)
#    print(end_index)
#    print('\n')
    t = 0
    while((t <= len(j) - 2) and (j[t] < j[t+1])):
      print("t: ", t)
      j[t], j[t+1] = j[t+1], j[t]
      t += 1
  
  return j
'''


def heap_sort(data):
  k = heaps()
  j = k.max_heap(data)
  
  #print(j)

  focus_index = 0
  insert_index = (len(j))

  while(insert_index > 1):
   # print(j)
   # print("ii: ", insert_index)
   # print("fi:", focus_index)
    l_c = (focus_index * 2) + 1
    r_c = (focus_index * 2) + 2 
    
    if(j[l_c] > j[focus_index]):
      #print("!!: ", j[l_c], j[focus_index]) 
      #print("II: ", insert_index)
      focus_index = l_c
    if(j[r_c] > j[focus_index]):
      focus_index = r_c
    
    #print("ii: ", insert_index)
    insert_index -= 1
    if(j[focus_index] > j[insert_index] and (focus_index < insert_index)):
      print(j)
      print("j_fi > j_ii: ",j[focus_index],j[insert_index])
      print("fi ii", focus_index, insert_index)
      print("\n")
      j.insert(insert_index, j.pop(focus_index))

    #print(j)
    #exit()
  
  return j


print(heap_sort(data))
