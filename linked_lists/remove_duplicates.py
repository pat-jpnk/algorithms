'''
task:

You're given the head of a Singly Linked List
whose nodes are in sorted order with respect
to their values. Write a function that returns a
modified version of the Linked List that doesn't
contain any nodes with duplicate values. The
Linked List should be modified in place (i.e., you
shouldn't create a brand new list), and the
modified Linked List should still have its nodes
sorted with respect to their values.

Each LinkedList node has an integer
value as well as a next node pointing to
the next node in the list or to None / null if
it's the tail of the list.

'''


class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def init_ll():
  ll_1 = LinkedList(1)
  ll_1.next = LinkedList(1)
  ll_1.next.next = LinkedList(1)
  ll_1.next.next.next = LinkedList(1)
  ll_1.next.next.next.next = LinkedList(3)
  ll_1.next.next.next.next.next = LinkedList(4)
  ll_1.next.next.next.next.next.next = LinkedList(4)
  ll_1.next.next.next.next.next.next.next = LinkedList(4)
  ll_1.next.next.next.next.next.next.next.next = LinkedList(5)
  ll_1.next.next.next.next.next.next.next.next.next = LinkedList(6)
  ll_1.next.next.next.next.next.next.next.next.next.next = LinkedList(6)
  return ll_1

'''

This solution is a lot more complicated than it needs to be,
it works even if the input linked list is not sorted!

Should have read the instructions

'''

def removeDuplicatesFromLinkedList(linkedList):
  cache = dict()
  cache[linkedList.value] = True
  idonotknow(linkedList, cache)
  return linkedList



def idonotknow(linkedList, cache):
  if(hasNext(linkedList)):
        
    if(linkedList.next.value in cache):
      
      if(hasNext(linkedList.next)):
        
        next_node = None
        cache_node = linkedList.next.next

        while(True):
          
          if(cache_node.value not in cache):
            next_node = cache_node
            break
          
          else:
            if(hasNext(cache_node)):
              cache_node = cache_node.next

            else:
              break

        if(next_node is None):
          linkedList.next = None
          return

        else:
          linkedList.next = next_node
          cache[linkedList.next.value] = True
          idonotknow(linkedList.next, cache)
    
      else:
        linkedList.next = None
        return 
    
    else:
      cache[linkedList.next.value] = True
      
      if not (hasNext(linkedList.next)):
        return 

      else:
        idonotknow(linkedList.next, cache)
    
  else:
    return


def hasNext(node):
  if(node.next == None):
    return False

  else:
    return True



'''

This was the suggested solution, much simpler

'''

def removeDuplicatesFromLinkedList_TWO(linkedList):
  current = linkedList

  while(current is not None):
    nextDistinctNode = current.next

    while(nextDistinctNode is not None and nextDistinctNode.value == current.value):
      nextDistinctNode = nextDistinctNode.next

    current.next = nextDistinctNode
    current = nextDistinctNode

  return linkedList


##### tests #####


def printList(linkedList):
  print(linkedList.value)
  if(linkedList.next is not None):
    print(" -> ")
    printList(linkedList.next)
  else:
    print(" -> ")
    print("None")


ll_1 = init_ll()

printList(ll_1)
print("\n\n")
removeDuplicatesFromLinkedList(ll_1)
print("\n\n")
printList(ll_1)
print("\n\n")


ll_1 = init_ll()
printList(ll_1)
print("\n\n")
removeDuplicatesFromLinkedList_TWO(ll_1)
print("\n\n")
printList(ll_1)
print("\n\n")
