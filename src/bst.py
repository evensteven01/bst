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

	def get_deepest(self, current_lvl: int) -> tuple:
		"""
			Gets the deepest nodes and their depths of this Node
			The format is (NodeCSV, Depth)
			where NodeCSV is is a comma seperated list of the deepest nodes
			and Depth is the depth of those nodes
		"""
		if not self.left and not self.right:
			return ([self.value], current_lvl)
		
		left_result = self.left.get_deepest(current_lvl+1) if self.left else ([],current_lvl)
		right_result = self.right.get_deepest(current_lvl+1) if self.right else ([],current_lvl)

		if left_result[1] == right_result[1]:
			return (left_result[0] + right_result[0], left_result[1])
		elif left_result[1] > right_result[1]:
			return left_result
		else:
			return right_result

	def __str__(self) -> str:
		return f'{self.value} {self.left} {self.right}'
				

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

	def get_deepest(self) -> tuple:
		"""
			Gets the deepest nodes and their depths.
			The format is (NodeCSV, Depth)
			where NodeCSV is is a comma seperated list of the deepest nodes
			and Depth is the depth of those nodes
		"""
		if self.root is None:
			return ([], None)
		else:
			return self.root.get_deepest(current_lvl=0)

	def __str__(self) -> str:
		""" Return a simple string representation of the binary search tree """
		return str(self.root)

if __name__ == '__main__':
	bst = BinarySearchTree([20, 14, 25, 23, 30, 26, 27])
	print(bst)
