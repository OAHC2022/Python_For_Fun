"""
BellmanFord Algorithm
It is very similar to Dijkstra Algorithm, but its slower and more robust
Time complexity: O(V*E)
it can detect negative cycles

Basically it runs iteration of (V-1) and every Iteration it update all the nodes from the edge list
***(nodes already with the minimum distance will not be updated as it is in Dijkstra Algorithm)
In the worst case (V-1) will be able to update all the nodes and get the minimum distance
So it will run one more time and check for every edge.
If a node has been updated again, then that means there is a negative cycle in the graph
"""

import sys

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencies_list = []
        self.predecessor = None
        self.min_dis = sys.maxsize
        self.visited = False

    def __str__(self):
        return str(self.name)


class Edge:
    def __init__(self, weight, start_vertex, end_vertex):
        self.weight = weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class BellmanFord:
    HAS_CYCLE = False
    def calc_shortest_path(self, nodes_list, edges_list, start_vertex):
        start_vertex.min_dis = 0

        for iterations in range(len(nodes_list) - 1):
            for edge in edges_list:
                start = edge.start_vertex
                end = edge.end_vertex

                tempdis = start.min_dis + edge.weight
                if tempdis < end.min_dis:
                    end.predecessor = start
                    end.min_dis = tempdis

        for edge in edges_list:
            start = edge.start_vertex
            end = edge.end_vertex

            tempdis = start.min_dis + edge.weight
            if tempdis < end.min_dis:
                BellmanFord.HAS_CYCLE = True
                print("Negative Cycle Detected")

    def get_shortest_path(self,end_vertex):
        if BellmanFord.HAS_CYCLE:
            print("Negative Cycle Detected")

        else:
            node = end_vertex
            while node:
                print(node)
                node = node.predecessor


if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")

    edge1 = Edge(5, node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    edge17 = Edge(1, node1, node2)
    edge18 = Edge(1, node2, node3)
    edge19 = Edge(-3, node3, node1)

    node1.adjacencies_list.append(edge1)
    node1.adjacencies_list.append(edge2)
    node1.adjacencies_list.append(edge3)
    node2.adjacencies_list.append(edge4)
    node2.adjacencies_list.append(edge5)
    node2.adjacencies_list.append(edge6)
    node8.adjacencies_list.append(edge7)
    node8.adjacencies_list.append(edge8)
    node5.adjacencies_list.append(edge9)
    node5.adjacencies_list.append(edge10)
    node5.adjacencies_list.append(edge11)
    node6.adjacencies_list.append(edge12)
    node6.adjacencies_list.append(edge13)
    node3.adjacencies_list.append(edge14)
    node3.adjacencies_list.append(edge15)
    node4.adjacencies_list.append(edge16)

    vertex_list = (node1, node2, node3, node4, node5, node6, node7, node8)
    # edge_list = (
    # edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15,
    # edge16)
    edge_list = (edge17, edge18, edge19)

    algorithm = BellmanFord()
    algorithm.calc_shortest_path(vertex_list, edge_list, node1)
    algorithm.get_shortest_path(node7)