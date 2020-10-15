import json
import socket

port = 9999
BUFSIZE = 1024
myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
ip_port = (myaddr, port)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp协议
server.bind(ip_port)
print("udp server正在运行", myaddr, port)

while True:
    data, client_addr = server.recvfrom(BUFSIZE)
    try:
        raw_data = data
        data = json.loads(data)
        code = data['code']
        msg = data['msg']
        print('状态码', code)
        print('消息', msg)
        print("请求地址：", client_addr)
        print("**********************")
        server.sendto(raw_data, client_addr)
    except Exception as e:
        str = "format is wrong"
        print("请求格式错误", e)
        print("请求地址：", client_addr)
        print("**********************")
        server.sendto(str.encode('utf-8'), client_addr)

server.close()
