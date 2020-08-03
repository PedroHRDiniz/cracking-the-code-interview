#Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks. 
class MyQueue:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def add(self, value):
		self.stack1.append(value)
	def peek(self):
		if len(self.stack2) != 0:
			return self.stack2[-1]
		if len(self.stack2) == 0:
			while(len(self.stack1) != 0):
				temp = self.stack1.pop()
				self.stack2.append(temp)
			return self.stack2[-1]
	def remove(self):
		if len(self.stack2) != 0:
			return self.stack2.pop()
		if len(self.stack2) == 0:
			while(len(self.stack1) != 0):
				temp = self.stack1.pop()
				self.stack2.append(temp)
			return self.stack2.pop()
	def isEmpty(self):
		return len(self.stack1) == 0 and len(self.stack2) == 0


myQueue = MyQueue()
myQueue.add('a')
myQueue.add('b')
myQueue.add('c')
myQueue.add('d')

myQueue.peek()
myQueue.remove()
myQueue.add('e')
myQueue.remove()
myQueue.remove()
myQueue.remove()
myQueue.remove()
myQueue.isEmpty()