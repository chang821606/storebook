"""
5.  实现方阵转置.(不定义函数)
    思想见图..
"""


# list01 = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16],
# ]

list01 = [
    [1,2,3],
    [5,6,7],
    [9,10,11],
]


"""
list01[1][0] <--> list01[0][1]
list01[2][0] <--> list01[0][2]
list01[3][0] <--> list01[0][3]
for r in range(1,4):
    list01[r][0] <--> list01[0][r]

list01[2][1] <--> list01[1][2]
list01[3][1] <--> list01[1][3]
for r in range(2,4):
    list01[r][1] <--> list01[1][r]
    
list01[3][2] <--> list01[2][3]
for r in range(3,4):
    list01[r][2] <--> list01[2][r]


for c in range(1,4):#1 2 3
    for r in range(c,4):
        list01[r][c-1] <--> list01[c-1][r]
 

for c in range(1,len(list01)):#1 2 3
    for r in range(c,len(list01)):
        list01[r][c-1] <--> list01[c-1][r]
10:35            
"""

for c in range(1,len(list01)):#1 2 3
    for r in range(c,len(list01)):
        list01[r][c-1],list01[c-1][r]= list01[c-1][r],list01[r][c-1]

print(list01)



