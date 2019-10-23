import redis
import pymysql
# 1.先到mysql更新update更新数据
# 2.缓存到redis中
# 2种情况: (1)redis中之前没有缓存 - 缓存(所有字段)
#         (2)redis中之前缓存过 - 直接更新字段

class Update(object):
    def __init__(self):
        self.db = pymysql.connect(
            'localhost','root','123456','userdb',
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        self.r = redis.Redis(
            host='localhost',port=6379,db=0
        )

    # 更新mysql表记录
    def update_mysql(self,wuqi,username):
        upd = 'update user set wuqi=%s where name=%s'
        try:
            self.cursor.execute(upd,[wuqi,username])
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print('Failed',e)

    # 更新redis
    def update_redis(self,username,wuqi):
        result = self.r.hgetall(username)
        # result非空: 更新wuqi字段
        # result为空: 到mysql查询,然后再缓存
        if result:
            self.r.hset(username,'wuqi',wuqi)
        else:
            self.select_mysql(username)

    def select_mysql(self,username):
        sel = 'select name,gender,wuqi from user where name=%s'
        self.cursor.execute(sel,[username])
        result = self.cursor.fetchall()
        # 同步到redis
        user_dict = {
            'gender':result[0][1],
            'wuqi':result[0][2],
        }
        self.r.hmset(username,user_dict)
        self.r.expire(username,30)

    # 主函数
    def main(self):
        username = input('请输入用户名:')
        wuqi = input('请输入新武器:')
        if self.update_mysql(wuqi,username):
            self.update_redis(username,wuqi)
        else:
            print('更新失败')

if __name__ == '__main__':
    syn = Update()
    syn.main()




