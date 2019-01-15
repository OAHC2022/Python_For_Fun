"""
Prims Algorithm
Find a starting node and push all the adjacent edges into a heap
then use greedy algorithm to find the edge with minimum weight linking an unvisited node
if the edge qualifies for the condition, then it will be added to the edge collection
find the next node and repeat the above steps until there are v-1 edges in the edge collection
"""
import heapq

class Graph:
    def __init__(self):
        self.edges = []
        self.vertices = {}

    def add_edge(self, weight, start, end):
        # Use this adjancencies_list method is pretty inefficient in coding
        if start not in self.vertices:
            self.add_node(start)
        if end not in self.vertices:
            self.add_node(end)
        startNode = self.vertices[start]
        endNode = self.vertices[end]
        self.edges.append(Edge(weight, startNode, endNode))
        self.vertices[start].adjacencies_list.append(self.edges[-1])
        self.vertices[end].adjacencies_list.append(self.edges[-1])


    def add_node(self, name):
        self.vertices[name] = Node(name)


class Edge:
    def __init__(self, weight, start, end):
        self.weight = weight
        self.start = start
        self.end = end

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight

    def __str__(self):
        return str(self.weight)


class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencies_list = []
        self.visited = False

    def __str__(self):
        return str(self.name)


class Prims:
    def calc_spanning_tree(self, G, node):
        heap = []
        new_spanning_tree = []

        for edge in node.adjacencies_list:
            heapq.heappush(heap,edge)

        node.visited = True

        while heap:
            the_edge = heapq.heappop(heap)

            # Since there is a problem in the graph that the edge's start and end is always fixed
            # I have to check which node is the one I need to iterate on
            if not the_edge.end.visited:
                node = the_edge.end
            elif not the_edge.start.visited:
                node = the_edge.start


            for edge in node.adjacencies_list:
                if not edge.end.visited and not edge.start.visited:
                    heapq.heappush(heap,edge)

            if not the_edge.end.visited or not the_edge.start.visited:
                # have to check if the edge are connecting two connected nodes
                new_spanning_tree.append(the_edge)
            node.visited = True

            if len(new_spanning_tree) == len(G.vertices)-1:
                break

        for edge in new_spanning_tree:
            print(edge.start, "---",edge.end)

if __name__ == "__main__":
    vertex1 = "a"
    vertex2 = "b"
    vertex3 = "c"
    vertex4 = "d"
    vertex5 = "e"
    vertex6 = "f"
    vertex7 = "g"

    G = Graph()
    G.add_edge(2, vertex1, vertex2)
    G.add_edge(6, vertex1, vertex3)
    G.add_edge(5, vertex1, vertex5)
    G.add_edge(10, vertex1, vertex6)
    G.add_edge(3, vertex2, vertex4)
    G.add_edge(3, vertex2, vertex5)
    G.add_edge(1, vertex3, vertex4)
    G.add_edge(2, vertex3, vertex6)
    G.add_edge(4, vertex4, vertex5)
    G.add_edge(5, vertex4, vertex7)
    G.add_edge(5, vertex6, vertex7)

    algorithm = Prims()
    algorithm.calc_spanning_tree(G,G.vertices[vertex7])



