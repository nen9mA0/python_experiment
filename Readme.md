# python物理实验计算库

该库提供了物理实验中常见的一些数据处理的函数

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

