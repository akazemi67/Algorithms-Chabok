# Problem's Link: https://quera.org/problemset/141574
MOD = 10 ** 9 + 7


def calc_pow2(p):
    if p == 0:
        return 1

    halfp = calc_pow2(p // 2)
    if p % 2 == 0:
        return (halfp * halfp) % MOD
    return (halfp * halfp * 2) % MOD


n, q = map(int, input().split())
sums = sum(map(int, input().split()))

sums = sums % MOD
for _ in range(q):
    num = int(input())
    result = (calc_pow2(num - n - 1) * sums) % MOD
    print(result)
