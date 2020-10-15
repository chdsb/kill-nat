import _thread
import datetime
import socket
import json
import threading
from multiprocessing import Process
import time

flag = True
aim_ip = None
aim_port = None
device_name = None


def create_server(server):
    while True:
        data, server_addr = server.recvfrom(1024)
        data = json.loads(data)
        code = data['code']
        msg = data['msg']
        if (code != 0):
            print('收到消息 ', msg)
            print('来源地址', server_addr)
            print("*******************")


def heart_beat(client):
    global flag
    while True:
        ip_port = ('服务器ip地址', 9999)
        data = {
            "code": 0,
            "device": device_name,
            "msg": "心跳" + str(datetime.datetime.now())
        }
        client.sendto(json.dumps(data).encode('utf-8'), ip_port)
        if flag:
            flag = False
            print(client.getsockname())
            threading.Thread(target=create_server, args=(client,)).start()
        time.sleep(5)


if __name__ == '__main__':
    globals
    device_name

    device_name = input("设备名称")

    BUFSIZE = 1024
    flag1 = True
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    threading.Thread(target=heart_beat, args=(client,)).start()
    flag = True
    while True:
        if flag1 == True:
            flag1 = False
            ip = input("ip: ")
            port = input("port: ")
            port = int(port)
        msg = input("msg: ")
        print(ip, port)
        ip_port = (ip, port)
        data = {
            "code": 1,
            "msg": msg
        }
        client.sendto(json.dumps(data).encode('utf-8'), ip_port)
    client.close()
