import http.client
import json


# 监播人气
def online(platId, roomId, roomurl):
    conn = http.client.HTTPConnection("139.196.120.113:6666")

    p = platId
    id = roomId
    url = roomurl

    payload = "{\"jsonrpc\":\"2.0\",\"method\":\"online\",\"id\":2022929231,\"params\":{\"p\":{},\"id\":{},\"url\":\"{}\"}}"
    # 把json数据load为字典
    payload = json.loads(payload)
    # print('payload',type(payload))
    # 对传递的参数进行赋值
    payload.get('params')['p'] = p
    payload.get('params')['id'] = id
    payload.get('params')['url'] = url
    # dump成字符串作为发送的
    payload = json.dumps(payload)

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "cc1153fa-80bf-9fb9-8f6f-01b45f81ba5a"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    online(2, 2461752, "https://www.douyu.com/2461752")
