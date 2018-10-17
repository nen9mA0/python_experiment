#Source of Data https://wenku.baidu.com/view/9d59440a844769eae009ed94.html

import sys
sys.path.append("..")
from exp import *

xl = [29.765,29.526,29.263,28.998,28.701,28.417,28.177,27.725,27.299,26.822]
xr = [18.931,19.110,19.429,19.692,19.972,20.278,20.013,20.963,21.388,21.856]

set_preci(0.001)
set_digit(5)

Dm = []
for i in range(len(xl)):
    Dm.append(float( format(xl[i]-xr[i],'-') ))
print Dm

M = []
for i in range(len(Dm)/2):
    M.append(float( format( format(Dm[i]**2,'*') - format(Dm[i+5]**2,'*')
print M