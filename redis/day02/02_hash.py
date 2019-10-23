import redis

r = redis.Redis(host='localhost',port=6379,db=0)

# 设置
r.hset('xiongba','name','niefeng')
# 更新
r.hset('xiongba','name','bujingyun')
# 获取
print(r.hget('xiongba','name'))
# HMSET : 多个field和value
user_dict = {
    'gender' : 'M',
    'wuqi': 'HaoJian'
}
r.hmset('xiongba',user_dict)

# HGETALL : 字典
print(r.hgetall('xiongba'))
# HKEYS : 列表
print(r.hkeys('xiongba'))
# HVALS : 列表
print(r.hvals('xiongba'))

# 删除field
r.hdel('xiongba','gender')
# 删除key
r.delete('xiongba')





































