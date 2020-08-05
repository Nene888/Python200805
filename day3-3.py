# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:57:45 2020

@author: USER
"""
name=[]
score=[]
total=0
avg=0
p=int(input("請輸入人數:　"))
for i in range(p):
    a=(input("請輸入名子:  "))
    name.append(a)
    s=int(input("請輸入分數: "))
    score.append(s)


def abb(p,total):
           
    avg=total/p
    return avg
for j in score:
    total=total+j 
ans = abb(p,total)
print(ans)
