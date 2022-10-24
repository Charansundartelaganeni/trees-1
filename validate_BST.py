#TC: O(n)
#SC: O(h) (height of the tree is h)

class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		stack = [(root, float('-inf'), float('inf'))] #initialize a stack with root and two negative infinity values
		while stack: #while the queue is not empty
			node, left, right = stack.pop(0)  #pop the stack and assign the values to left and right respectively
			if not left < node.val < right: #if the value of the node doen't lie between left and right, that means it is not a valid binary tree
				return False
			if node.left:
				stack.append((node.left, left, node.val)) #if there's left node, append node.left as root, left as left node and value of the current node as right value
			if node.right:
				stack.append((node.right, node.val, right)) #if there's right node, append node.right as root, right as rightt node and value of the current node as left value 
		return True #if loop exits, then the given tree is a valid binary tree