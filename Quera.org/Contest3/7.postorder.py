# Problem's Link: https://quera.org/problemset/356

def build_post_order(pre_order, in_order):
    if not pre_order:
        return []

    root = pre_order[0]
    root_index = in_order.index(root)

    left_post_order = build_post_order(pre_order[1:1 + root_index], in_order[:root_index])
    right_post_order = build_post_order(pre_order[1 + root_index:], in_order[root_index + 1:])
    return left_post_order + right_post_order + [root]


input()
in_order = input().split()
pre_order = input().split()

post_order = build_post_order(pre_order, in_order)
print(' '.join(post_order))

