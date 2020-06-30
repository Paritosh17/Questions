class Node: 
           
    def __init__(self, key): 
        self.key = key  
        self.left = None
        self.right = None
      
def lca(root, n1, n2): 
          
    if root is None: 
        return None
   
    if root.key == n1 or root.key == n2: 
        return root  
      
    left_lca = lca(root.left, n1, n2)  
    right_lca = lca(root.right, n1, n2) 
  
    if left_lca and right_lca: 
        return root  
 
    return left_lca if left_lca is not None else right_lca 
   
root = Node(2) 
root.left = Node(1) 
root.right = Node(3) 
root.right.left = Node(4) 
root.right.right = Node(5)
root.right.right.right = Node(6) 

print ("LCA(1,5) = ", lca(root, 1, 5).key )
print ("LCA(3,6) = ", lca(root, 3, 6).key) 
print ("LCA(4,6) = ", lca(root, 4, 6).key)
