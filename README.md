# BST
Binary Search Tree in Python

## Introduction
This is an implementation of a binary search tree in python.

It has two classes. The Node class is the main class that provides the functionality of a BST.

The BinarySearchTree class provides a nice wrapper representing what should be represented as an entire tree, with a root. It also provides useful entry points to the functionalities of the tree.

## Example usage:
The following will implement a Binary Search tree, adding the values in order they appear.
The resulting tree will have 10 at root, 7 as a left child, and 15 as a right child.

`bst = BinarySearchTree([10, 7, 15]`

You can add more values as such:

`bst.add(12)`

Or remove:

`bst.remove(7)`

We can search:

`bst.search(15)`

We can check if the BinarySearchTree contains a certain value:

`bst.contains(15)`

Finally, we can get the deepest nodes, and their depth, as follows:

`bst = BinarySearchTree([26, 82, 16, 92, 33])`

`result = bst.get_deepest()`

The result will be a tuple with the deepest values and their depth:

`([33,92],2)`


 
 
