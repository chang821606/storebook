"""
    练习：
    在控制台中获取一个月份，年份。
    打印当月的天数。
    1 3 5 7 8 10 12 -->  31天
    2 -> 闰年29天，平年28天。
    4 6 9 11 --> 30天
"""

year = int(input("请输入年份："))
month = int(input("请输入月份："))  # 15
if month < 1 or month > 12:
    print("月份输入有误")
elif month == 2:
    # result = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    # if result:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29天")
    else:
        print("28天")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30天")
else:  # 1 3 5 7 8 10 12
    print("31天")
