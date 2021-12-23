# Stack Last In, First Ou

# Using a List Method. Issues: slows down as input Information Grows.

stack = []
stack.append('3')
stack.append('carr')
stack.append('c')

print(stack)

print(stack.pop())
print(stack)

#  Implement Stack using Queue MOdule, Using a LIFO Queue

from queue import LifoQueue

# Created a stack

stack = LifoQueue(maxsize=3)
# Print the Size
print(stack.stack.size)


# Use Put() push element into Stack
stack.put('a')
stack.put('b')
stack.put('c')
stack.put('d')

# Take out elements
print(stack.get())
print(stack.get())
print(stack.get())





#  Implementing A QUEUES using QUeue.Queue. Using a built-in moduel of python
from queue import Queue

# Initializing a Queue with it size
queue = Queue(maxsize=4)
print(queue.queuesize())

# Add elements to the Queue
queue.put('Jump')
queue.put('Jump1')
queue.put('Jump2')
queue.put('Jump3')

# Return a boolean for full
print(queue.full)

# Remove element from Queue
print(queue.get())
print(queue.get())

# Check if it empty
# Return boolean
print(queue.empty())

