import http.client
import json

# 房间截屏
def screenshot_nb(id, total_time, interval_time, room_url):
    conn = http.client.HTTPConnection("192.168.120.85:4001")

    id = id
    total_time = total_time
    interval_time = interval_time
    room_url = room_url

    payload = "{\"jsonrpc\":\"2.0\",\"method\":\"screenshot_nb\",\"params\":{\"id\":{},\"total_time\":{},\"interval_time\":{},\"room_url\":\"{}\"},\"id\":200}"
    # 把json数据load为字典
    payload = json.loads(payload)
    # print('payload',type(payload))
    # 对传递的参数进行赋值
    payload.get('params')['id'] = id
    payload.get('params')['total_time'] = total_time
    payload.get('params')['interval_time'] = interval_time
    payload.get('params')['room_url'] = room_url


    # dump成字符串作为发送的url
    payload = json.dumps(payload)

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "15f00825-b393-4fa7-c9f8-7dd10d5881b2"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    screenshot_nb(321,20,2,"http://www.panda.tv/act/baozoumanhua20160824.html")

# payload = "{\"jsonrpc\":\"2.0\",\"method\":\"screenshot_nb\",\"params\":{\"id\":321, \"total_time\":20, \"interval_time\":2, \"room_url\":\"http://www.panda.tv/act/baozoumanhua20160824.html\"},\"id\":200}"
