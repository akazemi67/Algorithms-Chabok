items = [64, 68, 40, 44, 56, 12, 17, 21, 25, 28, 33, 36, 70, 3, 5, 10, 47, 50]


# 73, 73, 73, 73, 75, 75, 75, 76, 76, 77, 77, 78, 78, 80, 80, 80, 80
def dummy_two_sums(arr, expected_sum):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            curr_sum = arr[i] + arr[j]
            if curr_sum == expected_sum:
                print(f"{arr[i]} + {arr[j]} == {curr_sum}")


def good_two_sums(arr, expected_sum):
    binsearch = __import__("03_binary_search")
    n = len(arr)
    sorted_arr = sorted(arr)
    for i in range(n):
        idx = binsearch.recursive_bin_search(sorted_arr,
                                             expected_sum - sorted_arr[i],
                                             i + 1, n - 1)
        if idx >= 0:
            print(f"{sorted_arr[i]} + {sorted_arr[idx]} == {expected_sum}")


if __name__ == "__main__":
    dummy_two_sums(items, 80)
    print("-------------")
    good_two_sums(items, 80)
