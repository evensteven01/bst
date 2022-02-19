from src.bst import BinarySearchTree

def test_bst_empty():
	bst = BinarySearchTree()
	assert str(bst) == 'BST'