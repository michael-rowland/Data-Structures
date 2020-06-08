from linked_list import LinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self, storage=[]):
#         self.size = 0
#         self.storage = storage
    
#     def __len__(self):
#         if not self.storage:
#             return 0
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.insert(0, value)

#     def dequeue(self):
#         if not self.storage:
#             return None
#         return self.storage.pop()

class Queue:
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
            current = current.get_next()
            self.size += 1
        return self.size

    def enqueue(self, value):
        return self.storage.add_to_tail(value)

    def dequeue(self):
        return self.storage.remove_head()
