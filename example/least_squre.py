#Source of Data https://wenku.baidu.com/view/70794716fab069dc51220106?from=search

import sys
import matplotlib.pyplot as plt
sys.path.append("..")
from exp import *

x = [1.9,2.0,2.1,2.5,2.7,2.7,3.5,3.5,4.0,4.0,4.5,4.6,5.0,5.2,6.0,6.3,6.5,7.1,8.0,8.0,8.9,9.0,9.5,10.0]
y = [1.4,1.3,1.8,2.5,2.8,2.5,3.0,2.7,4.0,3.5,4.2,3.5,5.5,5.0,5.5,6.4,6.0,5.3,6.5,7.0,8.5,8.0,8.1,8.1]

[k,b] = least_square(x,y)

print k,b

fig = plt.figure()
draw1 = fig.add_subplot(111)
draw1.scatter(x,y,s=4)

linex = range(11)
liney = [k*x+b for x in linex]

plt.plot(linex,liney)

plt.show()