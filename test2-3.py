# -*- coding:utf-8 -*-
#姓名：田宏
#学号：1403050119
#班级：通风2班

import math

T = 27
P = 3e-2
p = 4e-2
NA = 6.022e23K = 1.38e-23
n = P/K*T
m = p/n
M = m*NA
print 'n=',n,'m=',m

M = (P*K*T*NA)/p

print 'M=', M
