from math import *
r=0
a=input()
d=input()
try:
    a=float(a)
    d=float(d)
    try:
        r=sqrt((a*log(d,e))/(2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3)))))
        print(r)
    except:
        print("Вычисление невозможно")
except:
    print("Вычисление невозможно")

'''
from math import *
r=0
a=input()
d=input()
try:
    a=float(a)
    d=float(d)
    if d>0 and 1 >= (cos(log(d, e) - 31 * 10 ** (-3))) >= (-1) and (2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3))))!=0 and (a*log(d,e))/(2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3))))>0:
        r=sqrt((a*log(d,e))/(2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3)))))
        print(r)
    else:
        print("Вычисление невозможно")
except:
    print("Вычисление невозможно")
'''

'''
from math import *
r=0
a = float(input())
d = float(input())
if d>0 and 1 >= (cos(log(d, e) - 31 * 10 ** (-3))) >= (-1) and (2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3))))!=0 and (a*log(d,e))/(2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3))))>0:
    r=sqrt((a*log(d,e))/(2-pi+log(d,e)*(cos(log(d,e)-31*10**(-3)))))
    print(r)
else:
    print("Вычисление невозможно")
'''
