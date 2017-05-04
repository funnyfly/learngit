#!/usr/bin/python
#coding:utf-8
'''
本地客户端
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999))
#接收服务端欢迎消息
print s.recv(1024)

for data in ['cpf','zxy','funny']:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
