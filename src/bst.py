class BinarySearchTree:
	""" This is a binary search tree supporting integers. """
	def __init__(self, root: int=None):
		""" Create a binary search tree """
		self.value = None
		self.left = None
		self.right = None
		print(f'Initializing BST')
		if root:
			self.add(root)

	def add(self, value: int) -> bool:
		""" Add a value to the binary search tree """
		if self.value == None:
			self.value = value
		print(f'Adding {value}')

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
		if not self.value:
			return '_'
		bstStr = str(self.value) + ' '
		if not self.left:
			bstStr += '_ '
		if not self.right:
			bstStr += '_ '
		if self.left:
			bstStr += str(self.left)
		if self.right:
			bstStr += str(self.right)
		return bstStr

if __name__ == '__main__':
	bst = BinarySearchTree()
	bst.add(4)
	print(bst)
