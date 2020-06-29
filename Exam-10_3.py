top_side = int(input('上底＞ '))
bottom_side = int(input('下底＞ '))
height = int(input('高さ＞ '))


def area(top_side, bottom_side, height):
    return (top_side + bottom_side) * height / 2


print('台形の面積 :', area(top_side, bottom_side, height))
