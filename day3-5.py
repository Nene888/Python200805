# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:11:41 2020

@author: USER
"""




while True:
    print('-------------------------------------------------------')
    print('1.加法')
    print('2.減法')
    print('3.乘法')
    print('4.除法')
    print('5.離開')

    adw=int(ut("請輸入inp指令: "))
    
    if adw==1:
        n1=int(input("請輸入數字一: "))   
        n2=int(input("請輸入數字二: "))
        print(n1,'+', n2, '=', n1+n2)

    elif adw==2:
        n1=int(input("請輸入數字一: "))   
        n2=int(input("請輸入數字二: "))
        print(n1,'-', n2, '=', n1-n2)
    
    elif adw==3:
        n1=int(input("請輸入數字一: "))   
        n2=int(input("請輸入數字二: "))
        print(n1,'x',n2,'=',n1*n2)
    
    elif adw==4:
        n1=int(input("請輸入數字一: "))   
        n2=int(input("請輸入數字二: "))
        print(n1,'/',n2,'=',n1/n2)
    
    else:
        break
        