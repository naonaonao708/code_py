# 二分探索

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]


def binary_search(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return - 1

print(binary_search(data,90))


# バブルソート

data_2 = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]

for i in range(len(data_2)):
    for j in range(len(data_2) - i - 1): # ソート済みの部分以外でループ
        if data_2[j] > data_2[j + 1]:
            data_2[j], data_2[j + 1] = data_2[j + 1], data_2[j]

print(data_2)

change = True
for i in range(len(data_2)):
    if not change: # 交換が発生していなければ終了
        break
    change = False # 交換が発生していないものとする
    for j in range(len(data_2) - i - 1):
        if data_2[j] > data_2[j + 1]:
            data_2[j], data_2[j + 1] = data_2[j + 1], data_2[j]
            change = True # 交換が発生した

print(data_2)



