# 练习:在控制台中录入一个成绩，
# 判断等级(优秀、良好、及格、不及格、成绩有误).
score = float(input("请输入成绩："))
# if score >= 90 and score <= 100:
#     print("优秀")
# elif score >= 80 and score < 90:
#     print("良好")
# elif score >= 60 and score < 80:
#     print("及格")
# elif score >= 0 and score < 60:
#     print("不及格")
# else:
#     print("成绩有误")


#   90 <= x <= 100
# if 90 <= score <= 100:
#     print("优秀")
# elif 80 <= score < 90:
#     print("良好")
# elif 60 <= score < 80:
#     print("及格")
# elif 0 <= score < 60:
#     print("不及格")
# else:
#     print("成绩有误")

if score < 0 or score > 100:
    print("成绩有误")
elif 90 <= score:
    print("优秀")
elif 80 <= score:
    print("良好")
elif 60 <= score:
    print("及格")
else:
    print("不及格")










