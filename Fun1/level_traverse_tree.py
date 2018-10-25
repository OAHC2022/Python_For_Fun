"""
    Citation: https://www.geeksforgeeks.org/level-order-tree-traversal/
"""


class Node:
    def __init__(self, cargo):
        self.cargo = cargo
        self.left = None
        self.right = None
        self.height = -1

    def __str__(self):
        return str(self.cargo)


def traverse_tree_method1(root):
    """
    Takes the root/start of the tree, then traverse through the tree in the level order.
    Time complexity: O(n^2)
    :param root: the node of a tree to be traversed
    :return: None
    """
    h = height(root)  # gets how deep the farthest leaf is
    for i in range(1,
                   h + 1):  # traverse from the root to the leaf (it can go from leaf to root as well). Use iteration to go through each level.
        print("level", i)
        print_tree_order(root, i)


def height(tr):
    if tr is None:
        return 0
    lheight = height(tr.left)
    rheight = height(tr.right)

    if lheight > rheight:
        tr.height = lheight + 1
        return lheight + 1
    else:
        tr.height = rheight + 1
        return rheight + 1


def print_tree_order(root, level):
    if root is None: return
    if level == 1:
        print(root)
    else:
        print_tree_order(root.left, level - 1)
        print_tree_order(root.right, level - 1)


"""*************************************************"""


class Queue:
    def __init__(self):
        self.head = None
        self.last = None
        self.length = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        if cargo is None: return
        if self.length == 0:
            self.head = self.last = cargo
        else:
            new_node = cargo
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def remove(self):
        if self.length == 0:
            print("Nothing in the queue")
            return
        next_node = self.head.next
        self.head.next = None
        self.head = next_node
        self.length -= 1

def traverse_tree_method2(root):
    """
    This is definitely better than the first one in general except a few limitation. It uses the queue method to traverse
    The time complexity is O(n)
    :param the node of a tree to be traversed
    :return: None
    """
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0])
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

if __name__ == "__main__":
    nodes = []
    for i in range(1, 10):
        nodes.append(Node(i))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[4].left = nodes[7]
    nodes[4].right = nodes[8]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    print("This is the method 1")
    traverse_tree_method1(nodes[0])
    print()
    print("This is the method 2")
    traverse_tree_method2(nodes[0])
