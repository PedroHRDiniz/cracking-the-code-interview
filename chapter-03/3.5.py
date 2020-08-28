class MyQueue:
	def __init__(self):
		self.stack = []
		self.stackTemp = []

	def push(self, value):
		if not len(self.stack):
			self.stack.append(value)
			return
		topo = self.peek()
		while value > topo:
			temp = self.pop()
			self.stackTemp.append(temp)
			if len(self.stack):
				topo = self.peek()
			else :
				topo = value
		self.stack.append(value)
		while len (self.stackTemp) :
			temp = self.stackTemp.pop()
			self.stack.append(temp)
	def peek(self):
		return self.stack[len(self.stack) - 1]
	def pop(self):
		return self.stack.pop()
	def isEmpty(self):
		return len(self.stack) == 0
