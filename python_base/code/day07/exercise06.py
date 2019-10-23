# 3行5列二维列表
list01 = [
    [3, 3, 6, 8, 9],
    [1, 96, 2, 33, 54],
    [33, 0, 12, 34, 33],
]
# 练习1:将第二行的元素打印出来(一行一个)
for item in list01[1]:
    print(item)

# 练习2:将第一列的元素打印出来(一行一个)
# print(list01[0][0])
# print(list01[1][0])
# print(list01[2][0])
for r in range(len(list01)):  # 0 1 2
    print(list01[r][0])

# 练习3:将全部元素打印出来(3行5列)
for r in range(len(list01)):
    for item in list01[r]:
        print(item, end=" ")
    print()

# for row in list01:
#     for col in row:
#         print(col,end = " ")
#     print()
