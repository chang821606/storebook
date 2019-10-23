import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
r.sadd('user:1','qiaozhi','peiqi','danni')
r.sadd('user:2','qiaozhi','peiqi','lingyang')

r.sinterstore('interset','user:1','user:2')
result = r.smembers('interset')
r_set = set()
for res in result:
    r_set.add(res.decode())

print(r_set)
print('共同关注人数:',r.scard('interset'))














