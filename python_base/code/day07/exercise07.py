# 练习4：矩阵转置
# 根据list01生成list02(每一行，是list01的每一列),
list01 = [
    [3, 3, 6, 8, 9],
    [1, 96, 2, 33, 54],
    [33, 0, 12, 34, 33],
]

list02 = []
# 获取list01第一列，形成一维列表.赋值给list02
# list01[0][0]
# list01[1][0]
# list01[2][0]

# line = []
# for r in range(len(list01)):
#     line.append(list01[r][0])
# list02.append(line)
#
# line = []
# for r in range(len(list01)):
#     line.append(list01[r][1])
# list02.append(line)

#                  获取列数
# for c in range(len(list01[0])):#0
#     line = []
#     获取list01每列数据，赋值给line
#     for r in range(len(list01)):#012
#         line.append(list01[r][c])
#     将line赋值给list02
#     list02.append(line)

# 15:35
for c in range(len(list01[0])):
    list02.append([])
    for r in range(len(list01)):
        list02[c].append(list01[r][c])

print(list02)

















