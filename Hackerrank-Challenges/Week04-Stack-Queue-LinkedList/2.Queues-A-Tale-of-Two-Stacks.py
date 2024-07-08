#!/bin/python3
# Problem's Link: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem


class MyQueue(object):
    def __init__(self):
        self.front = 0
        self.q = []
    
    def peek(self):
        return self.q[self.front]
        
    def pop(self):
        d = self.q[self.front]
        self.front += 1
        return d
        
    def put(self, value):
        self.q.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

