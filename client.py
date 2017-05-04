#!/usr/bin/python
#coding:utf-8

import socket
#创建socket  AF_INET指定使用IPV4协议，SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接  Web服务标准端口：80，FTP:21
s.connect(('www.sina.com.cn',80))
#发送数据 内容格式必须符合HTTP标准
s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

#接收数据
buffer = []

while True:
    #每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = ''.join(buffer)
#关闭连接
s.close()

header,html = data.split('\r\n\r\n',1)
print header
#把接收到的数据写入文件
with open('sina.html','wb') as f:
    f.write(html)

