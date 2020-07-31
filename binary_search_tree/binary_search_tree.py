"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #if value < Node's value
        if value < self.value:
            #we need to go left
            #if there is not left child,
            if self.left is None: 
                #then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            #otherwise there is a child
            else:
                #call the left child's 'insert' method
                self.left.insert(value)
        #otherwise, value >= Node's value 
        else: 
            #we need to go right
            #if we see there is not right child,
            if self.right is None:
                #then we can wrap the value in a BSTNode and park it
                self.right = BSTNode(value)
            #otherwise there is a child 
            else:
                #call the right child's 'insert' method 
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        else:
            if self.value > target:
               if self.left is None:
                   return False
               return self.left.contains(target)
            else:
                if self.right is None:
                    return False
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value) 
        if self.right is not None:
           self.right.for_each(fn)
        if self.left is not None:
           self.left.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left is not None:
            self.left.in_order_print()

        print(self.value)
        
        if self.right is not None:
            self.right.in_order_print()

     
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        from collections import deque

        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()
            print(current.value)

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []
        stack.append(self)

        while len(stack) > 0:
            current = stack.pop()
            print(current.value)

            if current.left is not None:
                stack.append(current.left)
            if current.right is not None:
                stack.append(current.right)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
# bst = BinarySearchTree(1)
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
#bst.in_order_dft()
print("post order")
bst.post_order_dft()  
