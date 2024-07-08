#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    one = head
    two = head
    while one and two:
        one = one.next
        two = two.next
        if two:
            two = two.next
        if one and one==two:
            return True
    return False

