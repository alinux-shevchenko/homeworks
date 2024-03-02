# task_1
#Implement append, index, pop, insert methods for UnsortedList.
# Also implement a slice method, which will take two parameters 'start' and 'stop',
# and return a copy of the list starting at the position and going up to but not including the stop position.

class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        return self.items.append(item)

    def pop(self, index=None):
        if index is None:
            return self.items.pop(index)

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self,start, stop):
        return self.items[start:stop]


unsorted_list = UnsortedList()
unsorted_list.append('one')
unsorted_list.append('two')
unsorted_list.append('three')
print(unsorted_list.slice(0, 2))

# task_2
#Implement a stack using a singly linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        return self.top.data \
            if self.top is not None\
            else None


stack = Stack()
stack.push('one')
stack.push('two')
stack.push('three')
print(stack.pop())
print(stack.peek())

# task_3
#Implement a queue using a singly linked list.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None
        return temp.data


queue = Queue()
queue.enqueue('one')
queue.enqueue('two')
queue.enqueue('three')
print(queue.dequeue())