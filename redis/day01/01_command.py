import redis

# 1.连接到redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0)
# 2.调用方法 key_list:[b'name',b'age',b'score']
key_list = r.keys('*')
for key in key_list:
    print(key.decode())

print(r.type('teachers'))
# exists()返回值: 0 | 1
print(r.exists('spider:urls'))
# delete()
r.delete('teachers')

























