#!/usr/bin/python
#coding:utf-8
'''
快速排序算法
'''

def kp(arr,i,j):
    if i < j:
        base = kpgc(arr,i,j)
        kp(arr,i,base)
        kp(arr,base + 1,j)
def kpgc(arr,i,j):
    base = arr[i]
    while i < j:
        while i < j and arr[j] >=base:
            j -= 1
        while i < j and arr[j] < base:
            arr[i] = arr[j]
            i += 1
            arr[j] = arr[i]
    arr[i] = base
    return i

ls = [3,2,4,8,5]
kp(ls,0,len(ls)-1)
print ls

