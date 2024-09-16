# Problem's Link: https://quera.org/problemset/69903


def get_day(month, day):
    days = [0] + [31]*6 + [30]*5 + [29]
    res = 0
    for m in range(1, month):
        res += days[m]
    return res + day


m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
print(abs(get_day(m1, d1)-get_day(m2, d2)))

