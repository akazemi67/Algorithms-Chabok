#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/is-binary-search-tree/problem


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inOrder(root, items):
    if not root:
        return 
    inOrder(root.left, items)
    items.append(root.data)
    inOrder(root.right, items)

    
def check_binary_search_tree_(root):
    items = []
    inOrder(root, items)
    for i in range(1, len(items)):
        if items[i]<=items[i-1]:
            return False
    return True
    
