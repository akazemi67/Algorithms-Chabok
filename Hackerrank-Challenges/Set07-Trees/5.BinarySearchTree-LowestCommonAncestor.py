#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def find_path(root, path, val):
    if not root:
        return False
        
    path.append(root)
    if root.info==val:
        return True
    
    if val < root.info and find_path(root.left, path, val):
        return True
    if val > root.info and find_path(root.right, path, val):
        return True
    
    path.pop()
    return False
    

def lca(root, v1, v2):
    path1 = []
    path2 = []
    
    if (not find_path(root, path1, v1)) or (not find_path(root, path2, v2)):
        return None
        
    n1 = len(path1)
    n2 = len(path2)
    i = 0
    while i<n1 and i<n2:
        if path1[i].info != path2[i].info:
            break
        i += 1
    return path1[i-1]
    

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)

