# 练习：定义计算4位整数，每位相加和的函数

def each_unit_sum(number):
    """
        计算整数的每位相加和
    :param number: 4位整数
    :return: 相加的和
    """
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result


# number = int(input("请输入四位整数："))
# result = each_unit_sum(number)
# print("结果是：" + str(result))
print(each_unit_sum(1234))
print(each_unit_sum(3456))
