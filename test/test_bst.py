from src.bst import BinarySearchTree

def test_bst_empty():
	""" Check that a BST starts off empty """
	bst = BinarySearchTree()
	assert str(bst) == '_'

def test_bst_initialize():
	""" Check that we can initialize a BST with a value """
	bst = BinarySearchTree(3)
	assert str(bst) == '3 _ _ '

def test_bst_initialize():
	""" Check that we can initialize a BST, then add a value """
	bst = BinarySearchTree()
	bst.add(3)
	assert str(bst) == '3 _ _ '
