#!/usr/bin/python
# coding:utf-8
'''
创建python中的堆栈
'''

class Stack(object):
    def __init__(st,size):
        st.stack = []
        st.top = -1
        st.size = size
    def empty(st):
        if st.top == -1:
            return True 
        return False 

    def full(st):
        if st.top == st.size:
            return True 
        return False

    def push(st,contect):
        if st.full():
            print 'stack is full'
            return False
        st.top = st.top + 1
        st.stack.append(contect)

    def pull(st):
        if st.empty():
            print 'stack is empty'
            return False
        st.top = st.top - 1
