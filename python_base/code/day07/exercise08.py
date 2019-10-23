# 练习: 实现两个列表全排列(结果：一个新列表)
# ["香蕉","苹果","哈密瓜"]
# ["雪碧","可乐","牛奶"]
list01 = ["香蕉", "苹果", "哈密瓜"]
list02 = ["雪碧", "可乐", "牛奶"]
list_result = [r + c for r in list01 for c in list02]
print(list_result)
