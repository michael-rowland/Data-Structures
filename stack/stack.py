from linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return 0 if not self.storage else len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         return None if not self.storage else self.storage.pop()

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if not self.storage.head:
            return 0
        if self.storage.head is self.storage.tail:
            return 1
        current = self.storage.head
        # WE PUT THIS IN BECAUSE WE KNOW THERE IS AT LEAST 1 AND OUR WHILE LOOP
        # LOOKS AT THE NEXT ITEM
        self.size = 1
        while current.get_next() is not None:
            self.size += 1
            current = current.get_next()
        return self.size

    def push(self, value):
        return self.storage.add_to_tail(value)

    def pop(self):
        return self.storage.remove_tail()
