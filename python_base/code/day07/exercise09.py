#练习：定义在终端中打印矩形的函数.
def print_rectangle(row_count,col_count,char):
    for r in range(row_count):
        for c in range(col_count):
            print(char,end =" ")
        print()# 换行


print_rectangle(2,3,"*")
#
print_rectangle(5,10,"8")

