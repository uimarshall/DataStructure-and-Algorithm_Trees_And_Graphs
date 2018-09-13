#-------------------------------------------------------------------------------
# Name:  Implement a binary heap as a max heap.
# Purpose:   educational
#
# Author:      mmk and marshal
#
# Created:     10/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------


class BinHeap:

    '''This class implement the Binary heap using max heap method'''

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
        self.size=0

    def perc_up(self,i):
        ''' implement the max heap method here'''
        while i // 2 > 0:
              #here is where we implement the max heap method
          if self.heap_list[i] > self.heap_list[i // 2]:
             #tmp = self.heapList[i // 2]
             tmp=self.heap_list[i]
             #self.heapList[i // 2] = self.heapList[i]
             self.heap_list[i]=self.heap_list[i // 2]
             #self.heapList[i] = tmp
             self.heap_list[i // 2]=tmp
          i = i // 2


    def insert(self,k):
      ''' implement the max heap method here'''
      self.heap_list.append(k)
      self.current_size = self.current_size + 1
      self.perc_up(self.current_size)


    def perc_down(self,i):
      while (i * 2) <= self.current_size:
          mc = self.min_child(i)
          #max heap implementation done here
          #if self.heapList[i] > self.heapList[mc]:
          if self.heap_list[i] < self.heap_list[mc]:
              #tmp = self.heapList[i]
              tmp = self.heap_list[mc]
              #self.heapList[i] = self.heapList[mc]
              self.heap_list[mc] = self.heap_list[i]
              self.heap_list[i] = tmp
          i = mc

    def min_child(self,i):
      if i * 2 + 1 > self.current_size:
          return i * 2
      else:
          #max heap implementation done here
          #if self.heapList[i*2] < self.heapList[i*2+1]:
          if self.heap_list[i*2] > self.heap_list[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1


    def del_min(self):
      retval = self.heap_list[1]
      self.heap_list[1] = self.heap_list[self.currentSize]
      self.current_size = self.current_size - 1
      self.heap_list.pop()
      self.perc_down(1)
      return retval


    def build_heap(self,alist):
      i = len(alist) // 2
      self.current_size = len(alist)
      self.heap_list = [0] + alist[:]
      while (i > 0):
          self.perc_down(i)
          i = i - 1
      return self.heap_list

def main():

    bh = BinHeap()
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(15)
    bh.insert(21)
    bh.insert(2)
    print(bh.heap_list)
    #print(bh.buildHeap([9,5,6,2,3]))

   # print(bh.delMin())
    #print(bh.delMin())
    #print(bh.delMin())
    #print(bh.delMin())
    #print(bh.delMin())

if __name__ == '__main__':
    main()
