#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping
#冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
#走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端。
def Msort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                print(list)
        print(list)

a = [5,4,3,2,1,9,8,6,77,0,]
Msort(a)

#冒泡排序
def bulubulu(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
a = [21,4,31,5,6]
bulubulu(a)
print(a)
