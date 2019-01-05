class Node:
    def __init__(self,name):
        self.name = name
        self.adjacency = []
        self.visited = False
        self.predecesor = None

    def __str__(self):
        return str(self.name)


class BFS:
    def search(self,start_node):
        self.queue = [start_node]
        start_node.visited = True
        while self.queue:
            node = self.queue.pop(0)
            print(node)
            for n in node.adjacency:
                if not n.visited:
                    self.queue.append(n)
                    n.visited = True

if __name__ == "__main__":
    nodes = []
    for i in range(5):
        nodes.append(Node(i))

    nodes[0].adjacency.append(nodes[2])
    nodes[0].adjacency.append(nodes[1])
    nodes[1].adjacency.append(nodes[3])
    nodes[2].adjacency.append(nodes[4])
    bfs = BFS()
    bfs.search(nodes[0])