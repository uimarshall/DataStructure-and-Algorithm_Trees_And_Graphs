#-------------------------------------------------------------------------------
# Name: Using the BinaryHeap class, implement a new class called PriorityQueue.
# Purpose: Education
#
# Author:      mmk and marshal
#
# Created:     11/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------

class Queue:
    '''Implementing the queue class that will be called in the PriorityQueue class'''

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)







class PriorityQueue:

    '''The main class that uses queue implimentation to built a binary heap'''

    def __init__(self):
        self.qeue =Queue()
        #adding a default item
        self.qeue.enqueue(0)
        #return it as a list to the self.heap_list
        self.heap_list = self.qeue.items
        self.current_size = 0


    def perc_up(self,i):


        while i // 2 > 0:

          if self.heap_list[i] < self.heap_list[i // 2]:
             tmp = self.heap_list[i // 2]
             self.heap_list[i // 2] = self.heap_list[i]
             self.heap_list[i] = tmp
          i = i // 2

    def insert(self,k):
      #implement the enqueue method here and it to the heap_list to ensure is place at the front of the list...

      self.qeue.enqueue(k)
       #dequeue method to take it out of the queue and transfer it to the list.
      self.heap_list.append(self.qeue.dequeue())

      self.current_size = self.current_size + 1
      self.perc_up(self.current_size)

    def perc_down(self,i):
      while (i * 2) <= self.current_size:
          mc = self.min_child(i)
          if self.heap_list[i] > self.heap_list[mc]:
              tmp = self.heap_list[i]
              self.heap_list[i] = self.heap_list[mc]
              self.heap_list[mc] = tmp
          i = mc

    def min_child(self,i):
      if i * 2 + 1 > self.current_size:
          return i * 2
      else:
          if self.heap_list[i*2] < self.heap_list[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1


    def del_min(self):
      retval = self.heap_list[1]
      self.heap_list[1] = self.heap_list[self.current_size]
      self.current_size = self.current_size - 1
      # implement a
      self.qeue.dequeue()
      #self.heapList.pop()
      self.heap_list=self.qeue.items
      self.perc_down(1)
      return retval


    def build_heap(self,alist):


      i = len(alist) // 2
      self.current_size = len(alist)
      self.heap_list = [0] + alist[:]
      while (i > 0):
          self.perc_down(i)
          i = i - 1
      return alist










def main():
    #pass
    h=Queue()
    h.enqueue(2)
    h.enqueue(4)
    h.enqueue(5)
    #print(h.items)
    k=PriorityQueue()
    #insert items
    k.insert(2)
    k.insert(4)
    k.insert(5)
    k.insert(6)
    print("list before 2 was  deqeue is   ",k.heap_list)
    # del  time
    k.del_min()

    print()
    print("list after 2 was  deqeue is   ",k.heap_list)

    #run test for the builtheap
    #print(k.build_heap(k.heap_list))

if __name__ == '__main__':
    main()
