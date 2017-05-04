#!/usr/bin/python
# coding:utf-8

import hashlib

db = {
    'michael': '4297f44b13955235245b2497399d7a93', #123123
    'bob': 'e10adc3949ba59abbe56e057f20f883e',    #123456
    'alice': '96e79218965eb72c92a549dd5a330112'   #111111
}

def calc_md5(user,password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()
def login(user,password):
    db_pwd = calc_md5(user,password)
    if db_pwd == db[user]:
        print 'login success'
        return True
    else:
        print 'password wrong'
        return False

user = raw_input('please input your username:')
password = raw_input('please input your password:')
if user in db:
    login(user,password)
else:
    print 'the username has not register'
