numerics = list(map(float, input('数値＞ ').split()))


def sum_total(numerics):
    return sum(numerics)


def average(numerics):
    return sum_total(numerics) / len(numerics)


def maxinum_value(numerics):
    return max(numerics)


print('平均 :', average(numerics))
print('最大値 :', maxinum_value(numerics))
