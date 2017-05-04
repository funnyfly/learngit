#!/usr/bin/python
#coding: utf-8

'''
服务器端
'''

import socket
import threading
import time
#创建socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#监听端口
s.bind(('127.0.0.1',9999))
#listen参数为指定连接的最大数量
s.listen(5)
print 'Waiting for connection...'


def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello,%s!' % data)
    sock.close()
    print 'connection from %s:%s is closed.' % addr

while True:
    #接受一个新连接
    sock,addr = s.accept()
    #创建新线程来处理TCP连接
    t = threading.Thread(target = tcplink,args = (sock,addr))
    t.start()

