# Tree

A tree is a data structure that consists of nodes connected by pointers. It is a widely used data structure that resembles a tree in nature, with a single node known as the root and other nodes branching out from it.

## EXAMPLE OF TREE

Here is an example of binary tree, it is a tree that links to no more than two other nodes.

![guess_design](tree.jpeg)

Node: Each element in the tree is called a node. Nodes can have zero or more child nodes.

Root: The topmost node of the tree, which does not have any parent nodes.

Parent and Child: A node that is connected to another node directly below it is considered the parent, while the connected node is its child.

Leaf: Nodes that do not have any child nodes are referred to as leaf nodes or terminal nodes.

Subtree: A subtree is a portion of the tree that consists of a node and all its descendants.

Here is an example of binary search tree:

![guess_design](tree2.jpeg)

When searching for a specific value in a binary search tree, comparisons are made at each node to determine whether to continue searching in the left or right subtree. By following the ordering property, the search operation can be performed by traversing only a fraction of the tree, resulting in a time complexity of O(log n) on average for search operations.

Using the tree above, we can determine where to put additional items. We always start at the root node and compare the new value with it. We keep comparing until we have found an empty place for the new node. For example, to insert the value 20, do the following:

Start at the root node 15 and compare with the new value 20

Since 20 is greater than 15, goto the right and visit node 24

Since 20 is less than 24, goto the left and see there is no additional node

Insert 20 in the empty spot to the left of 24.


## TREE IN PYTHON


```python
def insert(self, data):
	"""
	Insert 'data' into the BST.  If the BST
	is empty, then set the root equal to the new 
	node.  Otherwise, use _insert to recursively
	find the location to insert.
	"""
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):
	"""
	This function will look for a place to insert a node
	with 'data' inside of it.  The current subtree is
	represented by 'node'.  This function is intended to be
	called the first time by the insert function.
	"""
	if data < node.data:
		# The data belongs on the left side.
		if node.left is None:
			# We found an empty spot
			node.left = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the right subtree.
			self._insert(data, node.right)

```

```python
def __iter__(self):
	"""
    Perform a forward traversal (in order traversal) starting from 
    the root of the BST.  This is called a generator function.
    This function is called when a loop	is performed:

	for value in my_bst:
		print(value)

	"""
	yield from self._traverse_forward(self.root)  # Start at the root

def _traverse_forward(self, node):
	"""
	Does a forward traversal (in-order traversal) through the 
	BST.  If the node that we are given (which is the current
	subtree) exists, then we will keep traversing on the left
	side (thus getting the smaller numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the right side (thus getting the larger numbers last).

	The use of the 'yield' will allow this function to support loops
	like:

	for value in my_bst:
		print(value)

    The keyword 'yield' will return the value for the 'for' loop to
    use.  When the 'for' loop wants to get the next value, the code in
    this function will start back up where the last 'yield' returned a 
    value.  The keyword 'yield from' is used when our generator function
    needs to call another function for which a `yield` will be called.  
    In other words, the `yield` is delegated by the generator function
    to another function.

	This function is intended to be called the first time by 
	the __iter__ function.
	"""
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)

```

The table below shows the common functions in a BST.

![guess_design](tree3.png)



## Example Code: Finding Common Colors

Imagine you have collections of colored objects, and you want to compare collections and find common colors. 

You can use a set to accomplish this efficiently. Here's a simple code example:

```python
# Create sets for unique colors in two collections
colors_set1 = {'red', 'blue', 'green', 'yellow'}
colors_set2 = {'blue', 'yellow', 'purple', 'pink'}

# Find common colors using set intersection
common_colors = colors_set1 & colors_set2

# Display the common colors
print("Common Colors:")
for color in common_colors:
    print(color)

# Calculate the number of common colors
num_common_colors = len(common_colors)
print(num_common_colors)

```
In this scenario, we have two sets, colors_set1 and colors_set2, representing unique colors in two different collections. We want to compare these sets to find the common colors.

We use the intersection() method to find the common colors between the two sets. The resulting set, common_colors, contains only the colors that exist in both sets.

Finally, we display the common colors by iterating over the common_colors set and printing each color. We also calculate the number of common colors by obtaining the length of the set using len().

This program demonstrates how sets and set operations can be used to efficiently compare collections and find common elements, such as common colors between two sets.

## Problem to Solve : Merging Email Lists

Write a program to merge two email marketing lists from different sources and create a consolidated list without any duplicate email addresses.


You can check your code with the solution here: [Solution](set.py)



[Back to Welcome Page](0-Welcome.md)



