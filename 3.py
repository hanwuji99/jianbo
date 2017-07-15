import http.client
import json
def record(platform_id,room_id,source_link,duration,type):
    platform_id = platform_id
    room_id = room_id
    source_link =source_link
    duration = duration
    type = type

    conn = http.client.HTTPConnection("139.196.120.113:6666")

    payload = "{\"jsonrpc\":\"2.0\",\"method\":\"record\",\"id\":2022929231,\"params\":{\"platform_id\":{},\"room_id\":{},\"source_link\":\"{}\",\"duration\":{},\"type\":{}}}"
    payload = json.loads(payload)

    payload.get('params')['platform_id'] = platform_id
    payload.get('params')['room_id'] = room_id
    payload.get('params')['source_link'] = source_link
    payload.get('params')['duration'] = duration
    payload.get('params')['type'] = type

    payload = json.dumps(payload)




    headers = {
    'cookie': "6N3e_f2ec_saltkey=tJN85wwy;  6N3e_f2ec_lastvisit=1492145493;  6N3e_f2ec_visitedfid=39;  Hm_lvt_2772005b8bc0b193d080228322981977=1492149167,1492481277,1492657830;  6N3e_f2ec___XHLTXZ__<www>=d5ceL4FsNq4BP9m5GJgI472QjV1fUaqKpHK5mtY4bA1Bhin%2FdOyzGp%2BoPH2P9nEP2%2BxddKPZ6YxSCUU%2FZ3M%2BpBTp%2BqxVknj6zHU7g7xekg; 6N3e_f2ec_auth=76c6Aj3W2apZVEVcF9IexRIthcgp1ISMu5oSbv8HEGmxdG1yH6HcxdpjVotevla40YcTJV9UAziaRSKtzJ7i1dBwEc12xaXfg%2Fxd; Hm_lvt_1c358b33dfa30c89dd3a1927a5921793=1492590845,1492590966,1492657830,1493107863; Hm_lpvt_1c358b33dfa30c89dd3a1927a5921793=1493107873; 6N3e_f2ec_creditnotice=0D0D2D0D0D0D0D0D0D560; 6N3e_f2ec_creditbase=0D0D0D0D0D0D0D0D0; 6N3e_f2ec_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; 6N3e_f2ec_sid=i6k435; 6N3e_f2ec_lip=116.226.16.143%2C1493107838; 6N3e_f2ec_lastact=1493107889%09us.php%09",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "e8f886c1-80bf-d632-d5c0-aace6d0305bd"
    }

    conn.request("POST", "/", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))

if __name__ == '__main__':
    record(2,2461752,"https://www.douyu.com/2461752")


        # {"jsonrpc":"2.0","method":"online","id":2022929231,"params":{"p":2,"id":2461752,"url":"https://www.douyu.com/2461752"}}

# 接口名：record
# 平台id：platform_id
# 房间id：room_id
# 直播间地址：source_link
# 时长：duration （传0代表手动停止，传非0则自动停止，单位秒）
# 类型：type （传start开始录制，传stop停止录制，传record_count返回当前正在录制的个数）
# 保存地址如何返回再讨论

# https://www.douyu.com/918415
# roomid：918415  platid：2
# 访问接口地址？

