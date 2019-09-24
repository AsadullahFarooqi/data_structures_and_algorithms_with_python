class Node:
	def __init__(self):
		

class Stack:
	
	def __init__(self):
		self.stack = []

	def add_to_stack(self, item):
		self.stack.append(item)


def stack_empty(s):
	if s.top == None:
		return True
	return False

def push(s, x):
	s.append(s)

def pop(s):
	if stack_empty(s):
		return "underflow"
	out = s[-1]
	s.remove(s[-1])
	return out
