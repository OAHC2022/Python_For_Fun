"""
Key take away:
AVL tree is only balanced if the data/nodes are added gradually (AKA the tree will balance itself with new insert or remove)
the subtree of the AVL tree will always be AVL tree as well (AKA the abs(left height - right height) <= 1)

for Insertion:
1. each data added will always be the leaf node first
2. if the tree becomes unbalanced due to the newly added node, it has to fall into four category:
left-left; left-right; right-right; right-left
* because the subnodes of the unbalanced node will always be: k+2 and k (a difference of 2)
* the subnode (grandson) of k+2 will always be k+1 and k (a difference of 1)
with above two laws: it can prove why there are only 4 scenarios and why the rotations can work

for remove:
due to the property of th avl tree, if the node to be removed and it has two nodes,
then there could only be two scenarios:
1. the predecessor is the leaf node
2. the predecessor has only one more left left node, so the recursion will only go twice at most

for balance:
if one node is unbalanced, be either its left or right child
that subnode will have balance not equal to 0
if balance of the subnode is smaller than 0, it is a right heavy
if balance of the subnode is greater than 0, it is a left heavy
* so there could be only one function to check if the tree is balanced or not

Thought Question:
We could use the method of AVL tree to balance a pre-existing non-balanced tree?
Maybe go from bottom to top and make it AVL along the way?
"""
import copy


class Node:
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.right = None
        self.left = None


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left = self.insertNode(data, node.left)
        elif data > node.data:
            node.right = self.insertNode(data, node.right)

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        return self.checkViolation(node)

    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.left) - self.calcHeight(node.right)

    def checkViolation(self, node):
        # check if the tree is still balanced
        balance = self.calcBalance(node)
        if balance > 1 and self.calcBalance(node.left) > 0:
            print("left-left situation")
            return self.rotateRight(node)

        if balance > 1 and self.calcBalance(node.left) < 0:
            print("left-right situation")
            node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        if balance < -1 and self.calcBalance(node.right) < 0:
            print("right-right situation")
            return self.rotateLeft(node)

        if balance < -1 and self.calcBalance(node.right) > 0:
            print("right-left situation")
            node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)
        return node

    def rotateLeft(self, node):
        print("node {} is being rotate left".format(node.data))

        tempRight = node.right
        grandsonLeft = tempRight.left

        node.right = grandsonLeft
        tempRight.left = node

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempRight.height = max(self.calcHeight(tempRight.left), self.calcHeight(tempRight.right)) + 1

        return tempRight

    def rotateRight(self, node):
        print("node {} is being rotate right".format(node.data))

        tempLeft = node.left
        grandsonRight = tempLeft.right

        node.left = grandsonRight
        tempLeft.right = node

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        tempLeft.height = max(self.calcHeight(tempLeft.left), self.calcHeight(tempLeft.right)) + 1

        return tempLeft

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)
        else:
            print("there is no root")

    def removeNode(self, data, node):
        if not node:
            print("there is not {} in the tree".format(data))
            return None

        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        else:
            if not node.left and not node.right:
                print("delete leaf node")
                del node
                return None
            if not node.left:
                print("delete node with right nodes")
                temp = node.right
                del node
                return temp
            if not node.right:
                print("delete node with left nodes")
                temp = node.left
                del node
                return temp

            print("delete node with both nodes")
            # replace the node with the predecessor node
            temp = copy.copy(self.findPredecessor(node.left))
            temp.left = node.left
            temp.right = node.right
            del node
            self.removeNode(temp.data, temp.left)
            temp.height = max(self.calcHeight(temp.left), self.calcHeight(temp.right)) + 1
            # recursively replace nodes with their predecessors
            return self.checkViolation(temp)

        node.height = max(self.calcHeight(node.left), self.calcHeight(node.right)) + 1
        return self.checkViolation(node)

    def findPredecessor(self, node):
        while node.right:
            node = node.right
        return node

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.left:
            self.traverseInOrder(node.left)
        print("Data {}. Height {}.".format(node.data, node.height))
        if node.right:
            self.traverseInOrder(node.right)


if __name__ == "__main__":
    root = AVL()
    root.insert(100)
    root.insert(50)
    root.insert(150)
    root.insert(25)
    root.insert(75)
    root.insert(125)
    root.insert(175)
    root.insert(12)
    root.insert(37)
    root.insert(63)
    root.insert(87)
    root.insert(101)
    root.insert(130)
    root.insert(170)
    root.insert(200)
    root.insert(10)
    root.insert(30)
    root.insert(80)
    root.insert(127)
    root.insert(173)
    root.insert(43)
    root.traverse()
    print("***********")
    root.remove(50)
    root.remove(43)
    root.remove(37)
    root.traverse()