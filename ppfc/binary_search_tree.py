class Tree_node :
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

 

    def insert_node(self, value) :
        if value < self.value :
            if self.left is None :
                self.left = Tree_node(value)
            else :
                self.left.insert_node(value)
        else :
            if self.right is None :
                self.right = Tree_node(value)
            else :
                self.right.insert_node(value)

    def find_value(self, value) :
        if self.value == value :
            print("Found !")
        elif value<self.value :
            if self.left is None :
                print("Value not in the tree !")
            else :
                print("\tleft")
                self.left.find_value(value)
        else :
            if self.right is None :
                print("Value not in the tree !")
            else :
                print("\tright")
                self.right.find_value(value)
            



tree = Tree_node(10)
tree.insert_node(5)
tree.insert_node(7)
tree.insert_node(23)
tree.insert_node(1)
tree.insert_node(5)
tree.insert_node(11)
tree.insert_node(2)


# print(tree.right.left.value)
tree.find_value(2)

