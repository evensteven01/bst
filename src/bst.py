from typing import Union

class Node:
	""" This repreesnts a single Node in a Binary Search Tree """
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		if self.value == value:
			return False
		elif value < self.value:
			if self.left is None:
				self.left = Node(value)
				return True
			else:
				return self.left.add(value)
		elif value > self.value:
			if self.right is None:
				self.right = Node(value)
				return True
			else:
				return self.right.add(value)
				

class BinarySearchTree:
	""" This is a binary search tree supporting integers. """
	def __init__(self, values: Union[int,list]=None):
		""" Create a binary search tree """
		self.root = None
		if isinstance(values,list) and len(values)>0:
			self.root = Node(values[0])
			for val in values[1:]:
				self.root.add(val)
		elif isinstance(values, int):
			self.root = Node(values)

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		if self.root == None:
			self.root = Node(value)
			return True
		else:
			return self.root.add(value)

	def remove(self, value: int) -> bool:
		""" Remove a value from the binary search tree """
		pass

	def contains(self, value: int) -> bool:
		""" Check if the binary search tree contains the value """
		pass

	def search(self, value: int) -> 'BinarySearchTree':
		""" Get the subtree of a binary search tree by value """
		pass

	def __str__(self) -> str:
		""" Return a simple string representation of the binary search tree """
		raise NotImplementedError('Not yet implemented')

if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.add(4)
