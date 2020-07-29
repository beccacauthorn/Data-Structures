"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        old_head = self.head
         # if the list is empty
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head 
            self.length = self.length + 1
        else:
            self.head.prev = ListNode(value)
            self.head = self.head.prev 
            self.head.next = old_head
            self.length = self.length + 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head
         # if the list is empty
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return old_head.value
        else:
            self.head = self.head.next
            self.head.prev = None        
            self.length = self.length - 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        old_tail = self.tail

        # if the list is empty
        if self.length == 0:
            self.head = ListNode(value)
            self.tail = self.head 
            self.length = self.length + 1
        else:
            self.tail.next = ListNode(value)
            self.tail = self.tail.next 
            self.tail.prev = old_tail
            self.length = self.length + 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        old_tail = self.tail

        # if the list is empty
        if self.length == 0:
            return

        # if there is only one element
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return old_tail.value

        self.tail = self.tail.prev
        self.tail.next = None        
        self.length = self.length - 1
        return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            return

        if node == self.tail:
            self.tail = node.prev

        old_head = self.head 
        left = node.prev
        right = node.next
        self.head = node  
        self.head.next = old_head 
        self.head.prev = None 
        old_head.prev = self.head 

        if left is not None:
            left.next = right
        if right is not None:
            right.prev = left 


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            return

        if node == self.head:
            self.head = node.next

        old_tail = self.tail
        left = node.prev
        right = node.next
        self.tail = node
        self.tail.prev = old_tail 
        self.tail.next = None
        old_tail.next = self.tail

        if left is not None:
            left.next = right
        if right is not None:
            right.prev = left 

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = self.length - 1
            return

        left = node.prev
        right = node.next
        if left is not None:
            left.next = right
        if right is not None:
            right.prev = left 

        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.length = self.length - 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if empty, return None
        if self.length == 0:
            return None 

        # return the max
        current = self.head
        running_max = current.value
        while current is not None:
            if current.value > running_max:
                running_max = current.value
            current = current.next
        return running_max