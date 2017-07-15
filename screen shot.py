import http.client

conn = http.client.HTTPConnection("192.168.120.85:4001")
# 这个是http的线上的
# http://58.253.70.65/

# 测试的 http://192.168.120.85/
#  192.168.120.85:4001

payload = "{\"jsonrpc\":\"2.0\",\"method\":\"screenshot_nb\",\"params\":{\"id\":321, \"total_time\":20, \"interval_time\":2, \"room_url\":\"http://www.panda.tv/act/baozoumanhua20160824.html\"},\"id\":200}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "15f00825-b393-4fa7-c9f8-7dd10d5881b2"
    }

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




