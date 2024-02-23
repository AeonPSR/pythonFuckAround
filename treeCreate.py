class TreeNode:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def insert(self, value):
		if self.root is None:
			self.root = TreeNode(value)
		else:
			self._insert_recursively(self.root, value)

	def _insert_recursively(self, node, value):
		if value < node.value:
			if node.left is None:
				node.left = TreeNode(value)
			else:
				self._insert_recursively(node.left, value)
		elif value > node.value:
			if node.right is None:
				node.right = TreeNode(value)
			else:
				self._insert_recursively(node.right, value)

	def display_elements(self):
		self._display_inorder(self.root)

	def find_max_value(self):
		if self.root is None:
			return None
		current = self.root
		while current.right:
			current = current.right
		return current.value

	def _display_inorder(self, node):
		if node:
			self._display_inorder(node.left)
			print(node.value)
		self._display_inorder(node.right)

tree = BinaryTree()
elements = [5, 3, 7, 12, 2, 4, 6, 8]
for element in elements:
    tree.insert(element)

print(f"Biggest value:{tree.find_max_value()}")