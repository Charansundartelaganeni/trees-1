#TC:O(n) 
#SC:O(1)


def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    self.flag = True
    self.prev = float("-inf")
    self.inorder(root)
    return self.flag

    
def inorder(self,root):
    #base condition
    if root==None:
        return
    

    self.inorder(root.left) #recursively call the inorder funtion on the left subtree
    
    if root.val<=self.prev: #check whether the current root value is less than or equal to prev
        self.flag = False  #if yes, set the flag as False          
    self.prev = root.val  #else, set your prev as root.val
    
    self.inorder(root.right)#recursively call the inorder funtion on the right subtree