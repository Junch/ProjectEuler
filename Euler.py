#!/usr/local/bin/python3
import math

def problem_13():
    data = []
    def getData():
        fp = open("problem13.txt", "r")
        for line in fp:
            line = line.rstrip()
            data.append(int(line))
    getData()
    s = str(sum(data))
    for i in range(10):
        print (s[i], end='') 

def problem_15():
    def pascal_row(n):
        r = [1]
        for i in range(1, n+1):
            r1 = [1 for j in range(i + 1)]
            for j in range(1, i):
                r1[j] = r[j] + r[j-1]
            r = r1[:]
        
        return r

    def lattice(n):
        p = 0
        for i in pascal_row(n):
            p += i*i
            
        return p

    print(lattice(20))

def problem_16():
    print(sum([int(x) for x in (str(2**1000))]))

def problem_17():
    dict = {}
    dict[1] = 'one'
    dict[2] = 'two'
    dict[3] = 'three'
    dict[4] = 'four'
    dict[5] = 'five'
    dict[6] = 'six'
    dict[7] = 'seven'
    dict[8] = 'eight'
    dict[9] = 'nine'
    dict[10] = 'ten'
    dict[11] = 'eleven'
    dict[12] = 'twelve'
    dict[13] = 'thirteen'
    dict[14] = 'fourteen'
    dict[15] = 'fifteen'
    dict[16] = 'sixteen'
    dict[17] = 'seventeen'
    dict[18] = 'eighteen'
    dict[19] = 'nineteen'
    dict[20] = 'twenty'
    dict[30] = 'thirty'
    dict[40] = 'forty'
    dict[50] = 'fifty'
    dict[60] = 'sixty'
    dict[70] = 'seventy'
    dict[80] = 'eighty'
    dict[90] = 'ninety'
    dict[1000] = 'onethousand'

    def calc2bits(s):
        total = 0
        num = 10*s[0] + s[1]
        if num in dict:
            total += len(dict[num])
        else:
            total += len(dict[s[0]*10]) + len(dict[s[1]])
        return total

    def calcNumber(num):
        s = [int(x) for x in str(num)]
        unit = len(s)
        wordlen = 0

        if (unit == 1):
            wordlen += len(dict[s[0]])
        elif (unit == 2):
            wordlen += calc2bits(s)
        elif (unit == 3):
            wordlen += len(dict[s[0]]) + len('hundred')
            if (s[1] == 0 and s[2] == 0):
                pass
            else:
                wordlen += len('and') 
                ss = [s[1],s[2]]
                wordlen += calc2bits(ss)
        return wordlen

    total = 0
    for i in range(1,1000):
        total += calcNumber(i)
    total += len(dict[1000])
    print (total)

def problem_18():
    data = []
    dict = {}
    def getData():
        fp = open("problem18.txt", "r")
        for line in fp:
            line = line.rstrip()
            a = [int(x) for x in line.split()]
            data.append(a)

    getData()
    m = len(data[-1])
    for i in range(m):
        for j in range(i+1):
            left = 0
            right = 0
            if (j>0):
                left = dict[(i-1,j-1)]
            if (j<i):
                right = dict[(i-1,j)]
            parent = max(left, right)
            dict[(i,j)] = parent + data[i][j]
    maxvalue = max(dict.values())
    print(maxvalue)

def problem_19():
    dict={1:31, 2:28, 3:31, 4:30, 5:31,6:30, \
          7:31, 8:31, 9:30,10:31,11:30,12:31}

    def isLeapYear(year):
        if (year % 400 == 0):
            return True
        if (year % 100 == 0):
            return False
        if (year % 4 == 0):
            return True
        return False 

    def daysPerYear(year):
        days = 365
        if isLeapYear(year):
            days = 366
        return days

    def daysFrom1900(year, month):
        days = 1
        for i in range(1, month):
            days += dict[i]
        if (month >= 3 and isLeapYear(year)):
            days += 1

        for i in range(1900, year):
            days += daysPerYear(i)
        return days

    sundays=0
    for i in range(1901, 2001): # I used 2000 first!
        for j in range(1, 13): # I used 12 first!
            days = daysFrom1900(i,j)
            if (days % 7 == 0):
                sundays += 1
                print("(%d,%d)"%(i,j))
    print (sundays)

def problem_22():
    data=[]
    def getData():
        buff=[]
        fp = open("problem22.txt","r")
        for line in fp:
            buff = line.split(",")
            data.extend([(lambda s:s.strip('"'))(x) for x in buff])
    
    def sortData():
        data.sort()

    def worth(word):
        s = [(lambda x:ord(x)- 64)(x) for x in word]
        return sum(s)

    getData()
    sortData()
    loop = len(data)
    i=1
    total=0
    while(i<loop+1):
        total += i*worth(data[i-1])
        i += 1
    print(total)

def problem_23():
    def divisors(num):
        if (num==1):
            return [1]

        l = math.ceil(num**0.5)
        divs=list(filter(lambda x:num%x==0, range(2,l)))
        s = [(lambda x:num//x)(x) for x in divs]
        divs += s
        divs.append(1)
        if (l**2 == num):
            divs.append(l)
        return divs

    maxnum = 28124
    #s = set(filter(lambda x:sum(divisors(x)) > x, range(2,28124)))
    s=[n for n in range(1,maxnum) if sum(divisors(n)) > n ]
    sums=set(a+b for a in s for b in s if a<=b and a+b<=maxnum)
    result = sum(n for n in range(1,maxnum) if n not in sums)
    #result = sum(set(range(1,maxnum)) - set(sums))
    print (result)

def problem_24():
    #print(math.factorial(10))
    num = 1000000 - 1
    s= []
    a = list(range(10))
    for i in range(10):
        f= math.factorial(9-i)
        m = num // f
        order = a[m]
        a.remove(order)
        s.append(order)
        num %= f
    print(s)
    v = 0
    for i in range(len(s)):
        v = v*10 + s[i]
    print(v)

def problem_25():
    a,b,c = 1,1,2
    term = 3
    while(c < 10**999):
        a = b
        b = c
        c = a + b
        term += 1
    print (term)

def problem_26():
    def cycle(n):
        multis=[]
        numerator = 1
        numerators=[]
        while (numerator not in numerators):
            numerators.append(numerator)
            numerator *= 10
            while (numerator<n):
                multis.append(0)
                numerator *= 10
            m = numerator // n
            multis.append(m)
            numerator =  numerator % n
            if numerator==0:
                return []
        index = numerators.index(numerator)
        return multis[index:]

    d = max([(len(cycle(x)), x) for x in range(1,1000)])[1]
    print(d)

def problem_27():
    def prime(n):
        if (n<2):
            return False
        return all(n % i != 0 for i in range(2, int(n**0.5)+1))
    
    def quadratic(a,b):
        n = 0
        while(True):
            m = n**2 + a*n + b
            if not prime(m):
                return n
            n += 1
    
    maxv=max([(quadratic(a,b),a,b) for a in range(-999,1000) for b in range(-999,1000)])
    print(maxv)
    print(maxv[1]*maxv[2])

def problem_28():
    def diagonal(m):
        s = 1
        for n in range(1, m, 2):
            s += 4*n*n+ 10*n + 10
        return s
        
    print(diagonal(1001))

def problem_30():
    def maxbits():
        n = 1
        while(10**n < 9**5*n):
            n += 1
        return n

    def fifthEqual(n):
        return sum([int(x)**5 for x in str(n)]) == n

    k = maxbits()
    nums= [n for n in range(2,10**k) if fifthEqual(n)]
    #nums = filter(lambda x: fifthEqual(x), range(2,10**k))
    print(sum(nums))

def problem_35():
    def prime(n):
        if (n==2):
            return True
        if (n<2 or n%2 == 0):
            return False
        l = math.ceil(n**0.5) + 1
        i = 3
        while(i < l):
            if (n % i==0):
                return False
            i += 2
        return True

    def circularPrime(n):
        if not prime(n):
            return False
        ss = [int(x) for x in str(n)]
        for i in range(len(ss)):
            ss.append(ss.pop(0))
            m = 0
            for num in ss:
                m = m*10 + num
            if not prime(m):
                return False
        return True

    limit = 1000000
    s=list(filter(lambda x:circularPrime(x), range(2,limit)))
    print(len(s))

def problem_67():
    data = []
    dict = {}
    def getData():
        fp = open("problem67.txt", "r")
        for line in fp:
            line = line.rstrip()
            a = [int(x) for x in line.split()]
            data.append(a)

    getData()
    m = len(data[-1])
    for i in range(m):
        for j in range(i+1):
            left = 0
            right = 0
            if (j>0):
                left = dict[(i-1,j-1)]
            if (j<i):
                right = dict[(i-1,j)]
            parent = max(left, right)
            dict[(i,j)] = parent + data[i][j]
    maxvalue = max(dict.values())
    print(maxvalue)

if __name__ == "__main__":
    #problem_13()
    #problem_15()
    #problem_16()
    #problem_17()
    #problem_18()
    #problem_19()
    #problem_22()
    #problem_23()
    #problem_24()
    #problem_25()
    #problem_26()
    #problem_27()
    problem_28()
    #problem_30()
    #problem_35()
    #problem_67()