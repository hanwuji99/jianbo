import http.client
# 监播人气
conn = http.client.HTTPConnection("139.196.120.113:6666")

payload = "{\"jsonrpc\":\"2.0\",\"method\":\"online\",\"id\":2022929231,\"params\":{\"p\":2,\"id\":2461752,\"url\":\"https://www.douyu.com/2461752\"}}"

headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "cc1153fa-80bf-9fb9-8f6f-01b45f81ba5a"
    }

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
