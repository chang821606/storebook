import redis

r = redis.Redis(host='127.0.0.1',port=6379,db=0)
r.rpush('teachers','Wang','Guo','Tao','Lv','Qi')
# LINSERT teachers after Guo Xu
r.linsert('teachers','after','Guo','Xu')
# result: 6
print(r.llen('teachers'))
# lrange: [b'Wang','Guo','Xu','Tao','Lv','Qi']
print(r.lrange('teachers',0,-1))
print(r.rpop('teachers'))
# [b'Wang','Guo','Xu','Tao','Lv']
r.ltrim('teachers',0,4)
# brpop : 超时不会抛出异常,返回None
while True:
    # result为元组: (b'teachers', b'Lv')
    result = r.brpop('teachers',1)
    if not result:
        break
    print(result)

r.delete('teachers')
























