"""
A better solution for hashtable when it comes to string
every node is a letter
by comparing each node we have three children:
the left one is smaller, middle one is the same, the right one is the bigger one
if mismatched, it will be quicker to find out
Use linked list to achieve
the end of the word (a node) will carry a value, so that this could achieve the dictionary look up
time complexity O(1)
also this algorithm supports sorting but I don't know how to yet
"""

class Node:
    def __init__(self, char):
        self.char = char
        self.middle = None
        self.left = None
        self.right = None
        self.value = None


class TST:
    def __init__(self):
        self.root = None

    def push(self, key, val):
        index = 0
        self.root = self.pushNode(self.root, key, val, index)

    def pushNode(self, node, key, val, index):
        if not node:
            node = Node(key[index])
        if node.char > key[index]:
            node.left = self.pushNode(node.left, key, val, index)
        elif node.char < key[index]:
            node.right = self.pushNode(node.right, key, val, index)
        elif index < len(key) - 1:
            node.middle = self.pushNode(node.middle, key, val, index + 1)
        else:
            node.value = val
        return node

    def get(self, key):
        index = 0
        return self.getNode(self.root, key, index)

    def getNode(self, node, key, index):
        if not node:
            return None
        if key[index] < node.char:
            return self.getNode(node.left, key, index)
        elif key[index] > node.char:
            return self.getNode(node.right, key, index)
        elif index < len(key) - 1:
            return self.getNode(node.middle, key, index + 1)
        else:
            return node.value


if __name__ == "__main__":
    tst = TST()

    tst.push("apple", 100)
    tst.push("orange", 200)
    tst.push("app",50)

    print(tst.get("app"))
