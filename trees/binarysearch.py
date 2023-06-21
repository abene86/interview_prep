import queue

class NodeTree:
    def __init__(self, data:int)->None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data:int)->None:
        self.root = NodeTree(data)

    def add(self, data:int)->None:
        self.helper_addTree(self.root, None, data)

    def helper_addTree(self, root:NodeTree, parent:NodeTree, data:int)->None:
        if root == None:
            node = NodeTree(data)
            if data > parent.data:
                parent.right = node
            elif data < parent.data:
                parent.left = node
            return
        if data > root.data:        
            self.helper_addTree(root.right, root, data)
        elif data < root.data:
            self.helper_addTree(root.left, root, data)

    def print_levelorder(self):
        bus = queue.Queue(maxsize=0)
        bus.put(self.root)
        while not bus.empty():
            root = bus.get()
            if root != None:
                print(root.data, end=" ")
                bus.put(root.left)
                bus.put(root.right)
            else:
                print(root, end=" ")



def main():
    binarytree = BinarySearchTree(5)
    binarytree.add(2)
    binarytree.add(1)
    binarytree.add(3)
    binarytree.add(4)
    binarytree.add(7)
    binarytree.add(8)
    binarytree.add(6)
    binarytree.print_levelorder()

main()
