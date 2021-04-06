import socket

HOST = '127.0.0.1'  #标准的回环地址(localhost)
PORT = 65432        #监听的端口  (非系统级的端口:大于 1023)

#socket.AF_INET (IPv4)   sockets.SOCK_STREAM (TCP)
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))                     # 绑定IP地址与端口
    s.listen()                              # 监听
    conn,addr=s.accept()                    # 返回一个二元元组
    with conn:
        print('Connected by',addr)
        while True:
            data=conn.recv(1024)            # 一次接受1024字节个数据
            if not data:
                break
            conn.sendall(data)              # sendall() 发送全部

