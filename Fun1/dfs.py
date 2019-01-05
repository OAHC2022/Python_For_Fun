"""
BFS is implemented using queue
DFS is implemented using stack or recursion (recursion uses OS to do the stack job)
"""
class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.adjacency = []
        self.predecesor = None

    def __str__(self):
        return str(self.name)


class DFS:
    def search_stack(self,start_node):
        # go to the righmost node first
        self.stack = [start_node]
        start_node.visited = True
        while self.stack:
            node = self.stack.pop()
            print(node)
            for n in node.adjacency:
                if not n.visited:
                    self.stack.append(n)
                    n.visited = True

    def search_recursion(self,start_node):
        # go to the leftmost node first
        print(start_node)
        start_node.visited = True
        for n in start_node.adjacency:
            if not n.visited:
                self.search_recursion(n)

if __name__ == "__main__":
    nodes = []
    for i in range(5):
        nodes.append(Node(i))

    nodes[0].adjacency.append(nodes[2])
    nodes[0].adjacency.append(nodes[1])
    nodes[1].adjacency.append(nodes[3])
    nodes[2].adjacency.append(nodes[4])
    dfs = DFS()
    dfs.search_recursion(nodes[0])