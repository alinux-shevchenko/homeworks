# task_1
#Write a program that reads in a sequence of characters and prints them in reverse order,
# using your implementation of Stack.

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)

    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()

    return reversed_str

# Test
s = "Hello World!"
print("Original String: ", s)
print("Reversed String: ", reverse_string(s))


# task_2
#Write a program that reads in a sequence of characters,
# and determines whether it's parentheses, braces, and curly brackets are "balanced."

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

def is_balanced(s):
    stack = Stack()
    symbols = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in symbols:
            stack.push(char)
        else:
            if stack.is_empty() or symbols[stack.pop()] != char:
                return False

    return stack.is_empty()

# Test
s = "{[kaka]}"
print("Sequence: ", s)
print("Is balanced: ", is_balanced(s))


# task_3
#Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack.
# Any other element must remain on the stack respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

#Extend the Queue to include a method called get_from_queue that searches and returns an element e from a queue.
# Any other element must remain in the queue respecting their order.
# Consider the case in which the element is not found - raise ValueError with proper info Message

class Stack:
    def __init__(self):
        self.items = []

        def push(self, item):
            self.items.append(item)

        def pop(self):
            return self.items.pop()

        def get_from_stack(self, e):
            if e in self.items:
                self.items.remove(e)
                return e
            else:
                raise ValueError(f"{e} not found in stack")

#Test
s = Stack()
s.push("Hello")
s.push("World")
print(s.get_from_stack("Hello"))

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def get_from_stack(self, e):
        if e in self.items:
            self.items.remove(e)
            return e
        else:
            raise ValueError(f"{e} not found in queue")

# Test
q = Queue()
q.enqueue("Hello")
q.enqueue("World")
print(q.get_from_stack("World"))