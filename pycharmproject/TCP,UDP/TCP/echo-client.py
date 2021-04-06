import socket

HOST = '127.0.0.1'  #服务器的主机名或者IP地址
PORT = 65432        #服务器使用的端口

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))            # 连接IP与端口
    s.sendall(b'Hello World')         # sendall() 发送全部
    data=s.recv(1024)                 # 一次发送1024个字节

print('Received',repr(data))
