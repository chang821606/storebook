"""
    day08复习

    函数: [一个] 功能
    定义：
        def 函数名称(形式参数):
            ...
            return 数据

    调用：
        函数名称(实际参数)

    参数：调用者给定义者传递的消息

    返回值：定义者给调用者传递的结果
         return作用：返回数据，退出函数

    可变与不可变类型对象传参：
        不可变，函数内部修改栈帧的变量，不影响函数执行以后。
        可变，函数内部修改可变对象，影响函数执行以后。

    函数参数
        实参
            位置实参:根据位置进行对应(实-->形).
                序列实参:用星号拆分序列进行对应(元素-->形)
            关键字实参:根据名字进行对应(实-->形).
                字典实参:用双星号拆分字典进行对应(键-->形,传递值)
"""
def fun01(a,b):
    pass

fun01(1,2)

tuple01 = (3,5)
fun01(*tuple01)

fun01(b = 22,a= 11)

dict01 = {"b":222,"a":111}
fun01(**dict01)





