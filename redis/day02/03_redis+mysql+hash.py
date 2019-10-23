import redis
import pymysql

# 1.先到redis中查询
# 2.redis中没有,到mysql中查询
# 3.再缓存到redis中一份,设置过期时间30秒
# 4.再查一遍
r = redis.Redis(host='localhost',port=6379,db=0)
db = pymysql.connect(
    'localhost','root','123456','userdb',
    charset='utf8'
)
cursor = db.cursor()
# 开始 - 用户点击查询个人信息
username = input('请输入用户名:')
# redis查询
result = r.hgetall(username)
if result:
    print('redis:',result)
else:
    # redis中没有,需要到mysql中查询
    sel = 'select name,gender,wuqi from user ' \
          'where name=%s'
    cursor.execute(sel,[username])
    # result: (('bujingyun','M','haojian'),)
    result = cursor.fetchall()
    if result:
        print('mysql:',result)
        # 缓存到redis一份
        user_dict = {
            'gender' : result[0][1],
            'wuqi' : result[0][2]
        }
        r.hmset(username,user_dict)
        # 设置过期时间
        r.expire(username,30)
































