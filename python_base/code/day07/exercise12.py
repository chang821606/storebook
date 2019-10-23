# 练习：定义根据两，计算几斤零几两的函数
def get_weight_for_liang(liang_weight):
    jin = liang_weight // 16
    liang = liang_weight % 16
    return (jin,liang)# 借助容器返回多个结果

tuple_retult = get_weight_for_liang(25)
print("斤："+ str(tuple_retult[0]))
print("两："+ str(tuple_retult[1]))
