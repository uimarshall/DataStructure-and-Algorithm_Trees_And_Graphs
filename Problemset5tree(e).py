#-------------------------------------------------------------------------------
# Name: Using the buildHeap method, write a sorting function that can sort a list in
#       O(nlogn) time.

# Purpose:Education
#
# Author:      mmk and marshal
#
# Created:     11/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
class BinHeap:

    '''This class implement the Binary heap sorting function using min heap method'''

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):


        while i // 2 > 0:

          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2



    def insert(self,k):

      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1


    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def mergeSort(self,alist):
        #Implementating a merged sort of O(nlogn) Time
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            i=0
            j=0
            k=0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1

            while j < len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
            return alist

    def buildHeap(self,alist):
      ''' Implement the sorting method of O(nlogn) time.'''
       # we will implement a merge sort because it have a O(nlogn)
      self.mergeSort(alist)

      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1
      return alist

def main():

    bh = BinHeap()
    bh = BinHeap()
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    bh.insert(15)
    bh.insert(21)
    bh.insert(2)
    #print(bh.heapList)
    print(bh.buildHeap(bh.heapList))



if __name__ == '__main__':
    main()

