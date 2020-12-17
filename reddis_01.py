
#1.導入redis
import redis

if __name__ == '__main__':
    #創建redis的連接實例
    # 在連結外界時一定要用try
    try:
        rs = redis.Redis()
    except Exception as e:
        print(e)

    # 操作string
    # 添加set key value
    result = rs.set('name','itcast')
    print(result)

    #獲取
    name = rs.get('name')
    print(name)

