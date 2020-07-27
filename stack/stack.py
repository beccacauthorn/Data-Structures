"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack? an array is more memory intensive, the linked list you need to iterate a lot so probably less efficient 
"""
#class Stack:
    #def __init__(self):
        #self.size = 0
        #self.storage = []

    #def __len__(self):
        #return len(self.storage)

    #def push(self, value):
        #self.storage.append(value)

    #def pop(self):
        #if len(self.storage) > 0:
            #return self.storage.pop()
        #return None 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        #create the node from the value
        new_node = Node(value)
        #what do we do if tail is none?
        #what's the rule to set to indicate
        #the LinkedList is empty
        #check both head and tail to see if they are empty
        if self.head is None and self.tail is None:
            #both head and tail referring to same node
            self.head = new_node
            self.tail = new_node
        else:
            #these steps assume that the tail is already referring to a node
            #set the old tail's next to refer to the new node
            self.tail.set_next(new_node)
            #reassign self.tail to refer to the new node
            self.tail = new_node 

    def remove_head(self):
        #if the linkedlist is empty
        if self.head is None and self.tail is None:
            return
        #only single elem in the linked list
        #then both head and tail are pointing at same node
        if not self.head.get_next():
            head = self.head
            #delete linked list's head reference
            self.head = None 
            #delete linked list's tail reference
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        #set self.head to the Node after the head
        self.head = self.head.get_next()
        return value
    
    def remove_tail(self):
        #if there is an empty linked list
        if self.head is None and self.tail is None:
            return None

        #iterate over linked list until the second to last Node
        current = self.head 
        while current is not None and current.get_next() is not self.tail:
            current = current.get_next()

        #current is node right before the tail, set the tail to be none
        # keep the value before deleting it
        value = self.tail.get_value()
        # move self.tail to the node right before
        self.tail = current
        return value 

    def contains(self, value):
        current = self.head
        if current is None:
            return False 

        while current is not None:
            if current.get_value() == value:
                return True
            else:
                current = current.get_next()
        return False

    def get_max(self):
        # if empty, return None
        if self.head is None and self.tail is None:
            return None 

        # return the max
        current = self.head
        running_max = current.get_value()
        while current is not None:
            if current.get_value() > running_max:
                running_max = current.get_value()
            current = current.get_next()
        return running_max

class Stack:
    def __init__(self):
        self.size = 0 
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None 
