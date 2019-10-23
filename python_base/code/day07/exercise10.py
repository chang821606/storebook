# 练习：定义将一维列表中每个元素打印在终端的函数
# 例如：list01 = [44,4,5,5,6]
#      list02 = [“a”,"bbb",6]

def print_list(list_target):
    for item in list_target:
        print(item,end = " ")
    print()


list01 = [44, 4, 5, 5, 6]
print_list(list01)

list02 = ["a", "bbb", 6]
print_list(list02)