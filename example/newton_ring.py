#Source of Data https://wenku.baidu.com/view/9d59440a844769eae009ed94.html
#coding=utf-8
import sys
sys.path.append("..")
from exp import *

xl = [29.765,29.526,29.263,28.998,28.701,28.417,28.177,27.725,27.299,26.822]
xr = [18.931,19.110,19.429,19.692,19.972,20.278,20.714,20.963,21.388,21.805]    #这里改数据是因为原文算错了 = =

set_preci(0.001)
set_digit(5)

Dm = []
for i in range(len(xl)):
    Dm.append(format(xl[i]-xr[i],'-'))
print Dm

M = []
for i in range(len(Dm)/2):
    tmp = Dm[i]**2 - Dm[i+5]**2
    M.append(format(tmp,'-'))
print M

a_M = avr(M)          #这里差一位是因为原文算错了。。。，另外有效数字少一位就是float的锅了。。。它自动吧51.520输出为51.52

R = (a_M * 10**-6) / (4*25*5.893*10**-7)
set_digit(4)            #因为5.893
print("R = %s" %format(R,'/'))
deviation(M)


'''
print "....."
num = 51.519
x = [51.132,52.797,50.982,51.660,51.025]

num_sum = 0
for i in range(5):
    num_sum += (x[i]-num)**2
num_sum = num_sum / 4
print math.sqrt(num_sum)
'''                 #我佛了文库这个报告的数据到这完全算错了，上面是我验算的代码 = =