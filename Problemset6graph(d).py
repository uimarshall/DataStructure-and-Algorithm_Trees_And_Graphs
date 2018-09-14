#-------------------------------------------------------------------------------
# Name: Using breadth first search write an algorithm that can determine the shortest
#   path from each vertex to every other vertex.
# Purpose:  Education
#
# Author:      mmk and marshal
#
# Created:     13/09/2018
# Copyright:   (c) mmk 2018
# Licence:     <gloriaconcepto>
#-------------------------------------------------------------------------------

 class Graph:
    """
    Adjacency List implementation of a graph vertex
    We create a very simple class to represent or Graph nodes so we can use it in our Graph Traversal Algorithms
    Just the bare essentials were included here
    """
    def __init__(self, vert_id):
        """
        Constructor
        :param vert_id: The id that uniquely identifies the vertex.
        """
        self.vert_id = vert_id          # simple type
        self.neighbors = []             # type List[Vertex]
        self.status = 'undiscovered'    # undiscovered | discovered | explored

        self.distance = -1              # shortest distance from source node in shortest path search
        self.previous = None            # previous vertex in shortest path search

    def add_vertex(self, vertex):
        """
        Adds a new vertex as an adjacent neighbor of this vertex
        :param vertex: new Vertex() to add to self.neighbors
        """
        self.neighbors.append(vertex)

    def get_neighbors(self):
        """
        Returns a list of all neighboring vertices
        :return: list of vertexes
        """
        return self.neighbors




def shortestPathBFS(graph):
    """
    Shortest Path - Breadth First Search
    :param vertex: the starting graph node
    :return: does not return, changes in place
    """
    if graph is None:
        return

    queue = []                                  # our queue is a list with insert(0) as enqueue() and pop() as dequeue()
    queue.insert(0, graph)

    while len(queue) > 0:
        current_vertex = queue.pop()                    # remove the next node in the queue
        next_distance = current_vertex.distance + 1     # the hypothetical distance of the neighboring node

        for neighbor in current_vertex.get_neighbors():

            if neighbor.distance == -1 or neighbor.distance > next_distance:    # try to minimize node distance
                neighbor.distance = next_distance       # distance is changed only if its shorter than the current
                neighbor.previous = current_vertex      # keep a record of previous vertexes so we can traverse our path
                queue.insert(0, neighbor)


def traverseShortestPath(target):
    '''
    Traverses backward from target vertex to source vertex, storing all encountered vertex id's
    :param target: Vertex() Our target node
    :return: A list of all vertexes in the shortest path
    '''
    vertexes_in_path = []

    while target.previous:
        vertexes_in_path.append(target.vert_id)
        target = target.previous

    return vertexes_in_path



"""
the output for the sample graph should be:
shortest path length:  3
shortest path:  [8, 10, 7]
"""

def main():
   # pass
   # Build a graph to use in our example shortest path search
# This is done roughly just for the example here to get the structure illustrated.
# In practice, you will probably be given a pre made graph or build it more elegantly programmatically
     vertice_1 = Graph(1)
     vertice_2 = Graph(2)
     vertice_3 = Graph(3)
     vertice_4 = Graph(4)
     vertice_5 = Graph(5)
     vertice_6 = Graph(6)
     vertice_7 = Graph(7)
     vertice_8 = Graph(8)
     vertice_9 = Graph(9)
     vertice_10 = Graph(10)

     vertice_1.add_vertex(vertice_2)
     vertice_2.add_vertex(vertice_3)
     vertice_3.add_vertex(vertice_4)
     vertice_3.add_vertex(vertice_5)
     vertice_5.add_vertex(vertice_6)
     vertice_6.add_vertex(vertice_7)
     vertice_1.add_vertex(vertice_8)
     vertice_8.add_vertex(vertice_9)
     vertice_8.add_vertex(vertice_10)
     vertice_10.add_vertex(vertice_7)


    # Lets set out source and target vertexes and find the shortest path between them
     source = vertice_1
     target = vertice_7

    # Find the shortest path from our source vertex to every other vertex.
    # The path data should be saved by reference in each vertex and available to us afterwards
     shortestPathBFS(source)

    # Trace the shortest path back from the target vertex to the source vertex
     vertexes_in_path = traverseShortestPath(target)

    # Display the results
     print("shortest path length: ", len(vertexes_in_path) )

     # print our shortest path in reverse order - from source to target  vertexes_in_path[::-1]

     print("shortest path:",vertexes_in_path[::-1])


if __name__ == '__main__':
     main()



