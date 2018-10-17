# python物理实验计算库

该轮子提供了物理实验中常见的一些数据处理的函数

## set_win()

文档编码为utf-8，该参数用于设置回显中文为GBK（默认）

##set_unix()

## set_unix()

用于设置回显中文为utf

## format

**format(input, flag, num)**

对运算结果按照加减乘除规则进行修约

  * input:	待修约数字
  * flag:         采用的修约方式，'*'和/''或0根据有效数字位数修约，'+'和'-'或1根据小数点精度修约
  * num:       指定有效数字/小数点位数，当设置有效数字时输入有效数字位数，设置小数点位数时，如精确到小数点后两位则输入0.01，若为0使用默认set_digit和set_preci设置的精度

返回值： **string**

注意：为了保证返回值位数正确这里返回的是string，此处的有效数字化简是由Decimal模块实现的，若小数点位数值大于1全部会默认按照1进行化简（即保留0位小数）

## set_digit

**set_digit(num, echo=1)**

设置有效数字

* num:     有效数字位数
* echo:     默认回显

返回值：无

## set_preci

**set_preci(num, echo=1)**

设置精确度

* num:     精确度，最好为0.1的乘方（0.01，0.001）
* echo:     默认回显

返回值：无

## avr

**avr(num=[], flag=1,echo=1)**

求平均数

* num       list类型，待求的数据

* flag         为1时返回修约后结果，否则返回未修约结果

* echo       是否回显

返回值：**float**

## deviation

**deviation(num=[], flag=1, echo=1)**

求标准差

* num        list类型，待求的数据
* flag          为1时返回修约后结果，否则返回未修约结果
* echo        是否回显

返回值：**float**

## sigmax

**sigmax(num=[], flag=1, echo=1)**

求A类不确定度

* num         list类型，待求数据
* flag           是否对标准差使用修正参数进行修正
* echo         是否回显
  返回值：**float**

## datacheck

**datacheck(num=[], echo=1)**

使用3sigma原则筛值

* num        list类型，待筛数据
* echo       是否回显

返回值：筛完数据后的list



## uncertainty

**uncertainty(data, delta, echo=1)**

求不确定度

* data        list类型，待求数据
* delta       B类不确定度中的仪器不确定度
* echo       是否回显

返回值：**float**

## least_square

**least_squre(x, y)**

最小二乘法

* x             list类型，最小二乘的x值
* y             list类型，最小二乘的y值

返回值：[k,b]，k为斜率b为截距



## 注意：

* 这套代码是上学期刚做物理实验的时候老师讲了一堆繁琐的数据处理，脑抽花了大概一晚上写的，当时就有整理一下开源的想法但没什么时间，今天刚好有空又花了一晚上重新写了下format函数，改了下回显和之前因为编码而导致的一些乱码，但是对当时具体的计算过程也有点忘了，因此可能会有bug
* 此处B类不确定度只考虑了仪器不确定度，即直接使用 △仪 / 根号3 计算，若教材有公式请使用sigmax函数与B类不确定度公式进行计算
* **感觉处理有效数字上还是有点问题**

