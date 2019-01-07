"""
Why Use Min-Heap:
1. if the same node is pushed into the heap several times due to different paths
for example:
first a relative large one with distance 10, then a relative smaller one with distance 5, finally a smallest one with distance 2
use min heap to only calc the smallest one with 2 and then update its adjacencies
otherwise if use normal queue, all the adjacencies to that node will be updated 3 times which is undesired
(AKA update means push the adjacency nodes to the heap, so there will be less nodes existing in the heap using min-heap)

2. Use the Min-Heap Method can ensure that the visited node is already the best global optimum
everytime we visit a node with the least distance which can be proven that the node already has the least distance
in this way, we can be sure that the node can be marked as visited and we do not need to visit it again

***there is no way for that node to has a less distance otherwise it won't be the minimum in the heap

3. Because we use greedy algorithm, everytime we try to find the min distance,
then heap will be a handy algorithm due to its time complexity O(1) + O(logN) = O(logN)

Thought:
to avoid redudency of visiting nodes, maybe we could use hashmap?
"""
import heapq
import sys
class Edge:
	def __init__(self,weight,start_vertex,end_vertex):
		self.weight = weight
		self.start_vertex = start_vertex
		self.end_vertex = end_vertex

class Node:
	def __init__(self,name):
		self.name = name
		self.adjacencies_list = []
		self.visited = False
		self.predecessor = None
		self.min_dis = sys.maxsize

	def __cmp__(self, other):
		return self.cmp(self.min_dis,other.min_dis)

	def __lt__(self, other):
		return self.min_dis < other.min_dis

	def __str__(self):
		return str(self.name)

class Dijkstra:
	def calc_shortest_path(self,start_node):
		q = []
		start_node.min_dis = 0
		heapq.heappush(q,start_node)
		count = 0
		while q:
			node = heapq.heappop(q)
			if not node.visited:
				# to check if the node has been visited, it will improve the running complexity
				for edge in node.adjacencies_list:
					count +=1
					start = edge.start_vertex
					end = edge.end_vertex
					tempdis = start.min_dis + edge.weight
					if tempdis < end.min_dis:
						end.min_dis = tempdis
						end.predecessor = start
						heapq.heappush(q,end)
				node.visited = True

	def get_shortest_path(self,end_node):
		print("the shortest path length is {}".format(end_node.min_dis))
		node = end_node
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

	edge1 = Edge(5,node1,node2)
	edge2 = Edge(8,node1,node8)
	edge3 = Edge(9,node1,node5)
	edge4 = Edge(15,node2,node4)
	edge5 = Edge(12,node2,node3)
	edge6 = Edge(4,node2,node8)
	edge7 = Edge(7,node8,node3)
	edge8 = Edge(6,node8,node6)
	edge9 = Edge(5,node5,node8)
	edge10 = Edge(4,node5,node6)
	edge11 = Edge(20,node5,node7)
	edge12 = Edge(1,node6,node3)
	edge13 = Edge(13,node6,node7)
	edge14 = Edge(3,node3,node4)
	edge15 = Edge(11,node3,node7)
	edge16 = Edge(9,node4,node7)

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


	vertex_list = (node1,node2,node3, node4, node5, node6, node7, node8)

	algorithm = Dijkstra()
	algorithm.calc_shortest_path(node1)
	algorithm.get_shortest_path(node4)
