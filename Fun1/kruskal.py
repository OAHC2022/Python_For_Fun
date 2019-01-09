"""
Spanning Tree
A connected Graph can have multiple spanning tree
edge always equal to N - 1 (N is the number of nodes)
it cannot be greater nor less than N - 1
Spanning Tree does not have cycles
a complete graph can have maximum of N^(N-2) number of spanning trees
to finish one spanning tree, we have to remove e - N + 1 edges

--> Standard Algorithm Usually Use Greedy Algorithm

Kruskal Algorithm --> find the minimum spanning tree
Time Complexity: Worst case: E*LogE ; Average case: N*LogN
Disjoint set is an important concept in this problem.
At first we have all the vertices which each one stands for a distinct set
then, we sort the edges and use Greedy Algorithm to iterate through the edges
since each edge contains the start node and end node
we can compare if two nodes are in the same set or not
if not we add the edge and merge two sets into one
we repeat until there is only one set left which means it is a spanning tree already

Disjoint Set:
we use linked list to link nodes together. we can arbitrarily (but usually done in sequence) find one node as the parent node
then that parent node will represent all the nodes in the set
which means whenever we find a node in that set, we always iterate through the parent node and then find the parent node
we compare the parent nodes to determine whether any two nodes are in the same set or not

Two important function:
1. Find:
we iterate through the parent nodes to find the parent node
---> along the way we set all the subnodes link to the parent node directly
so that next time we can achieve O(1) time complexity to determine the set

2. Union
when we want to merge two sets together, we link one of the parent node to the other
how the nodes are linked depends on the height of each parent node
---> if they are the same, we can arbitrarily determine one but add the height to the parent one!
"""

class Graph:
    def __init__(self):
        self.edge_list = []
        self.set_num = 0
        self.vertex_dict = {}

    def add_vertex(self, name):
        node = Vertex(name)
        self.vertex_dict[name] = node
        self.set_num += 1

    def add_edge(self, weight, start, end):
        if start not in self.vertex_dict:
            self.add_vertex(start)
        if end not in self.vertex_dict:
            self.add_vertex(end)
        startNode = self.vertex_dict[start]
        endNode = self.vertex_dict[end]
        self.edge_list.append(Edge(weight, startNode, endNode))


class Vertex:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.height = 0

    def __str__(self):
        return str(self.name)


class Edge:
    def __init__(self, weight, start, end):
        self.start = start
        self.end = end
        self.weight = weight

    def __cmp__(self, other):
        return self.cmp(self.weight, other.weight)

    def __lt__(self, other):
        return self.weight < other.weight


class Disjoint_set:

    def find(self, vertex):
        node = vertex
        while node.parent:
            node = node.parent
        root = node

        # reset all the subsets
        node = vertex
        while node != root:
            temp = node.parent
            node.parent = root
            node = temp

        return root

    def union(self, vertex1, vertex2):
        x = self.find(vertex1)
        y = self.find(vertex2)

        if x == y:
            return

        if x.height > y.height:
            y.parent = x
        elif y.height > x.height:
            x.parent = y
        else:
            x.parent = y
            y.height += 1


class Kruskal:

    def find_min_spanning_tree(self, Graph):
        disjoint = Disjoint_set()
        edges = Graph.edge_list
        new_edge_list = []
        # greedy Algorithm ---> this step is very important
        edges.sort()

        for edge in edges:
            start = edge.start
            end = edge.end
            if disjoint.find(start) is not disjoint.find(end):
                disjoint.union(start, end)
                new_edge_list.append(edge)
                Graph.set_num -= 1
            if Graph.set_num == 1:
                break

        for edge in new_edge_list:
            print(edge.start, "---", edge.end)


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
    algorithm = Kruskal()
    algorithm.find_min_spanning_tree(G)
