#coding=utf-8
import sys
import math
import decimal as dc

digit = 3                                     #有效数字
preci = '0.01'                                     #精确度
                                       
_WIN_ = 1     

def set_win():
    _WIN_ = 0

def set_unix():
    _WIN_ = 1

def format(input , flag , num=0):                      #格式化（有效数字）                                                                      
    global preci
    global digit

    cache = str(input)
    
    if flag=='*' or flag=='/' or flag==0:
        if num != 0:
            dc.getcontext().prec = num

        ret = str( dc.Decimal(cache) / dc.Decimal('1') )
            
        if num != 0:
            dc.getcontext().prec = digit

    elif flag=='+' or flag=='-' or flag==1:
        tmp = dc.getcontext().prec
        dc.getcontext().prec = 30                   #防止报有效数字位数不够的错误
        if num != 0:
            ret = str( dc.Decimal(cache).quantize(dc.Decimal(str(num))) )
        else:
            ret = str( dc.Decimal(cache).quantize(dc.Decimal(preci)) )
        dc.getcontext().prec = tmp
    else:
        print "ERROR:parameter flag error,cannot do format"
    return ret

def set_digit( num , echo=1 ):
    global digit

    digit = int(num)
    dc.getcontext().prec = digit
    if echo==1:
        mystr = "有效数字位数为 %d"
        if _WIN_:
            mystr = mystr.decode('UTF-8').encode('GBK')
        print(mystr %(digit))


def set_preci( num , echo=1 ):
    global preci

    preci = str(float(num))
    if echo==1:
        mystr = "精确到小数点后 %d 位"
        if _WIN_:
            mystr = mystr.decode('UTF-8').encode('GBK')
        i = 0
        j = float(preci)
        while j < 1:
            i += 1
            j *= 10
        print(mystr %(i))

def avr( num=[] ,flag=1 ,echo=1 ):                     #平均值
    sum=0.0
    n=len(num)
    cache=0.0
    for i in num:
        sum+=float(i)

    cache=sum/n
    cache_b = format(cache,'+')

    if echo ==1:
        mystr1 = "平均值为%f"
        mystr2 = "修约后平均值为%s"
        if _WIN_:
            mystr1 = mystr1.decode('UTF-8').encode('GBK')
            mystr2 = mystr2.decode('UTF-8').encode('GBK')
        print(mystr1 %(cache))
        print(mystr2 %(cache_b) )

    if flag==1:
        return float(cache_b)
    else:   
        return cache



def deviation( num=[] ,flag=1 ,echo=1):                #标准差
    global preci,digit
    myavr = avr(num,1,0)
    n=len(num)

    sum = 0
    for i in num:
        cache = i-myavr
        sum += cache**2  

    cache = sum / (n-1)
    cache = math.sqrt(cache)
    
    sum=0
    for i in num:
        cache_b = float(format(i-myavr,'-'))
        sum += float(format(cache_b**2,'*'))

    cache_b = sum  / (n-1)
    
    cache_b = math.sqrt(cache_b)
   # cache_b = round(cache_b,)

    if echo==1:
        mystr1 = "标准差为 %f"
        mystr2 = "修约后标准差为 %f"
        if _WIN_:
            mystr1 = mystr1.decode('UTF-8').encode('GBK')
            mystr2 = mystr2.decode('UTF-8').encode('GBK')
        print(mystr1 %(cache))
        print(mystr2 %(cache_b))

    if flag==1:
        return cache_b
    else:   
        return cache


def sigmax( num=[] ,flag=1 ,echo=1):                   #A类不确定度Xa
    n = len(num)
    
    if flag==1:
        temp = 1
    else:
        t = [0,0,1.84,1.32,1.20,1.14,1.11,1.09,1.08,1.07,1.06,1.05,1.03]
        if n>=len(t) or n==1 or n==0:
            print "value t no found"
        else:
            temp = t[n]
            if echo==1:
                print("t = %f" %temp)

    cache = deviation(num,1,0)
    cache = temp * cache / math.sqrt(n)

    if echo==1:
        print("sigmax=%f" %(cache))
    return cache



def datacheck( num=[] , echo=1 ):                #3sigma筛值
    sigma=deviation(num,1,0)
    myavr=avr(num,1,0)
    upper=myavr+3*sigma
    lower=myavr-3*sigma

    if echo==1:
        print ("3sigma = %f" % (3*sigma))
        print ("upper %f" % (upper))
        print ("lower %f" % (lower))
    flag = False
    for i in num:
        if i>upper or i<lower:
            flag = True
            num.remove(i)
            if echo ==1:
                print "remove" %i
    
    if flag == True:
        num = datacheck(num)
    
    return num


def uncertainty( data ,delta,echo=1):                #合成不确定度
    if delta == 0:
        print "Input delta"
        delta = float(raw_input())
    xb = delta / math.sqrt(3)
    xa = sigmax(data,1,0)
    x = math.sqrt(xb**2 + xa**2)

    if echo==1:
        mystr = "仪器不确定度为 %f"
        if _WIN_:
            mystr = mystr.decode('UTF-8').encode('GBK')
        print(mystr %(x))
    return x


def least_square(x,y):
    lenx = len(x)
    leny = len(y)
    if lenx != leny:
        print "ERROR: x[] Not Equal y[]"
    
    sumxy = 0
    sumx2 = 0
    sumx = 0
    sumy = 0
    for i in range(0,lenx):
        sumxy += x[i]*y[i]
        sumx += x[i]
        sumy += y[i]
        sumx2 += x[i]**2
    
    k = (sumxy - sumx*sumy/lenx) / (sumx2 - (sumx**2)/lenx )
    b = sumy/lenx - k*sumx/lenx
    return [k,b]


