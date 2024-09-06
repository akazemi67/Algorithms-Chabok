# Problem's Link: https://quera.org/problemset/9722

def is_prime(num):
    p = 2
    while p * p <= num:
        if num % p == 0:
            return False
        p += 1
    return num >= 2


def generate_nums(idx, num, L):
    if idx == L:
        print(num)
        return

    for i in range(1, 10):
        tmp = 10 * num + i
        if is_prime(tmp):
            generate_nums(idx + 1, tmp, L)


n = int(input())
generate_nums(0, 0, n)

