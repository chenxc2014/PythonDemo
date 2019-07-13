# _*_ coding:utf-8 _*_
# author:chenxc
# datetime:2019/7/13 23:19
# function:


# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
server_socket.bind((host, port))

# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
    # 建立客户端连接
    client_socket, address = server_socket.accept()

    print("连接地址: %s" % str(address))

    msg = '欢迎访问菜鸟教程！' + "\r\n"
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()
