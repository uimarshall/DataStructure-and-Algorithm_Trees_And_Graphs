#-------------------------------------------------------------------------------
# Name:   Write the transpose method for the Graph class
# Purpose:  Education
#
# Author:      mmk and marshal
#
# Created:     13/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------
'''
   A transpose graph is a graph that edge are in reverse direction.In this
   implementation we assume the graph is directed and weighted.The graph class was
   modified to take care of weight.
'''


class Vertex:
        def __init__(self,key):
            self.id = key
            self.connectedTo = {}

        def addNeighbor(self,nbr,weight=0):
            self.connectedTo[nbr] = weight

        def __str__(self):
            return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

        def getConnections(self):
            return self.connectedTo.keys()

        def getId(self):
            return self.id

        def getWeight(self,nbr):
            return self.connectedTo[nbr]




class Graph:

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.cost =[]

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.cost.append(cost)


    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


def transpose_graph(graph):
      '''This function takes in a graph an return it's transpose'''
      transposeList=[]
      for v in graph:
        for w in v.getConnections():
           print("The transpose graph showing connections of vertices   :","( %s , %s )" % ( w.getId(),v.getId()))
           #print(v.getConnections())
            #add it to a list
           transposeList.append(w.getId())
           transposeList.append(v.getId())


      print("The transpose list :",transposeList)


def main():
    #pass
    g = Graph()

    for i in range(6):
      g.addVertex(i)

    g.addEdge(0,1,70)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    g.addEdge(5,2,1)

    for v in g:
        for w in v.getConnections():
           print("The original graph showing connections of vertices :","( %s , %s )" % (v.getId(), w.getId()))


    transpose_graph(g)




if __name__ == '__main__':
    main()