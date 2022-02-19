class BinarySearchTree:
	""" This is a binary search tree supporting integers. """
	def __init__(self, root: int=None):
		""" Create a binary search tree """
		pass

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		pass

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
		return "BST"

if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.add(4)
	print(bst)
