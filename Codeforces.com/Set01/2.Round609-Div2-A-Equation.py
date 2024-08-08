# Problem's Link: https://codeforces.com/contest/1269/problem/A


def is_composite(num):
    if num>2 and num%2==0:
        return True
    p = 3
    while p*p <= num:
        if num%p==0:
            return True
        p += 2
    return False
    
    
n = int(input())
a = 4
while True:
    b = a + n
    if is_composite(b):
        print(b,a)
        break
    a += 2

