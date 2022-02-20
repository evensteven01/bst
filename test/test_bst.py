from src.bst import BinarySearchTree

def test_bst_empty():
	""" Check that a BST starts off empty """
	bst = BinarySearchTree()
	assert bst.root is None

def test_bst_initialize():
	""" Check that we can initialize a BST with a value """
	bst = BinarySearchTree(3)
	assert bst.root.value == 3

def test_bst_add_one():
	""" Check that we can initialize a BST, then add a value """
	bst = BinarySearchTree()
	bst.add(3)
	assert bst.root.value == 3

def test_add_root_l_l():
	""" Check that adding 3 nodes place properly in root then left, left """
	bst = BinarySearchTree()
	bst.add(5)
	bst.add(4)
	bst.add(2)
	assert bst.root.left.left.value == 2

def test_add_root_r_r():
	""" Check that adding 3 nodes place properly in root then right, right """
	bst = BinarySearchTree(5)
	bst.add(5)
	bst.add(6)
	bst.add(10)
	assert bst.root.right.right.value == 10

def test_initialize_list():
	bst = BinarySearchTree([5,6,10])
	assert bst.root.right.right.value == 10

def test_add_root_duplicate():
	""" Check that adding duplicate results in not adding the node """
	bst = BinarySearchTree()
	bst.add(5)
	result = bst.add(5)
	assert result == False
	assert bst.root.value == 5

def test_depth_empty():
	bst = BinarySearchTree()
	result = bst.get_deepest()
	assert not result[0] and result[1] == None

def test_depth_example_1():
	bst = BinarySearchTree([12,11,90,82,7,9])
	result = bst.get_deepest()
	print(f'Result: {result}')
	assert result[0] == [9] and result[1] == 3

def test_depth_example_2():
	bst = BinarySearchTree([26, 82, 16, 92, 33])
	result = bst.get_deepest()
	assert result[0] == [33,92] and result[1] == 2

def test_remove_from_empty():
	bst = BinarySearchTree()
	result = bst.remove(4)
	assert result.root is None

def test_remove_non_existent():
	bst = BinarySearchTree([23,12,4,56])
	result = bst.remove(5)
	assert result is not None

def test_remove_no_children():
	bst = BinarySearchTree([20, 14, 25, 26])
	result = bst.remove(14)
	assert not bst.root.left

def test_remove_one_child():
	bst = BinarySearchTree([20, 14, 25, 26])
	result = bst.remove(25)
	assert bst.root.right.value == 26

def test_remove_two_children_successor_has_child():
	bst = BinarySearchTree([20, 14, 25, 23, 30, 26, 27])
	print(bst)
	result = bst.remove(25)
	print(bst)
	assert bst.root.right.value == 26
	assert bst.root.right.right.left.value == 27
	assert bst.root.right.left.value == 23

def test_remove_two_children_successor_is_child():
	bst = BinarySearchTree([20, 14, 25, 23, 27])
	print(bst)
	result = bst.remove(25)
	print(bst)
	assert bst.root.right.value == 27
	assert bst.root.right.right == None
	assert bst.root.right.left.value == 23

def test_remove_two_children_successor_no_child():
	bst = BinarySearchTree([20, 14, 25, 23, 28, 27])
	print(bst)
	result = bst.remove(25)
	print(bst)
	assert bst.root.right.value == 27
	assert bst.root.right.right.value == 28
	assert bst.root.right.left.value == 23

def test_search_empty_tree():
	bst = BinarySearchTree()
	result = bst.search(4)
	assert result and result.root is None

def test_search_not_in_tree():
	bst = BinarySearchTree(5)
	result = bst.search(4)
	assert result and result.root is None

def test_search_find():
	bst = BinarySearchTree([20, 14, 25, 23, 28, 27])
	result = bst.search(25)
	assert result and result.root.value == 25
	assert result and result.root.left.value == 23

def test_contains_empty():
	bst = BinarySearchTree()
	result = bst.contains(4)
	assert result is False

def test_contains_false():
	bst = BinarySearchTree([20, 14, 25, 23, 28, 27])
	result = bst.contains(4)
	assert result is False

def test_contains_true():
	bst = BinarySearchTree([20, 14, 25, 23, 28, 27])
	result = bst.contains(14)
	assert result is True