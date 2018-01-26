#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 斐波那契数列。

# 使用循环
def fib(n):
	a,b = 1,1
	for i in range(n-1):
		a,b = b,a+b
	return a

# 使用递归
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)

# 方法三
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


# 输出了第10个斐波那契数列
print fib(10)