import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
r.sadd('shengdoushi','xingshi','zilong')
# 数据类型: 集合 {b'zilong', b'xingshi'}
# {'zilong','xingshi'}
result = r.smembers('shengdoushi')
# 创建空集合
r_set = set()
for res in result:
    r_set.add(res.decode())

# print(r.spop('shengdoushi'))

r.sadd('shengdoushi2','xingshi','yadianna')

r.sinterstore('interset','shengdoushi','shengdoushi2')
print(r.smembers('interset'))
print('共同好友数:',r.scard('interset'))





























