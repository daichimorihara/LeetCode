"""
Implement a MyQueue class which implements a queue using two stack
"""


class MyQueue:
	def __init__(self):
		#supposing that Stack Class is imported
		self.new_stack = Stack()
		self.old_stack = Stack()

	def shift_stacks(self):
		if self.old_stack.is_empty():
			while not new_stack.is_empty():
				self.old_stack.push(self.new_stack.pop())

	def peek(self):
		if self.isempty():
			return False
		self.shift_stacks()
		return self.old_stack.peek()

	def remove(self):
		if self.isempty():
			return False
		self.shift_stacks()
		return self.old_stack.pop()






	def is_empty(self):
		return len(self) == 0

	def __len__(self):
		return len(self.new_stack) + len(self.old_stack)