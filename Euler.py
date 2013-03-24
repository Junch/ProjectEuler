#!/usr/local/bin/python3
import math
import time
import functools
import operator
from itertools import permutations

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

def problem_29():
    n = len(set(a**b for a in range(2,101) for b in range(2,101)))
    print(n)

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

def problem_31(): #Coin sums good problem
    """
    In England the currency is made up of pound, ?, and pence, p, and there are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, ?1 (100p) and ?2 (200p).
    It is possible to make ?2 in the following way:
    1?1 + 150p + 220p + 15p + 12p + 31p
    How many different ways can ?2 be made using any number of coins?
    """
    num = 200
    s=0
    for g in range(num//100 + 1):
        for f in range(num//50 + 1):
            gf = 100*g+50*f
            if (gf > num): break
            for e in range(num//20 + 1):
                gfe = 20*e + gf
                if (gfe > num): break
                for d in range(num//10 + 1):
                    gfed = 10*d+gfe
                    if (gfed > num): break
                    for c in range(num//5 +1):
                        gfedc = 5*c + gfed
                        if (gfedc > num): break
                        for b in range(num//2 + 1):
                            gfedcb = 2*b + gfedc
                            if (gfedcb > num): break
                            for a in range(num + 1):                       
                                if (a+gfedcb==num):
                                    s += 1
                                    break
    print (s+1)

def problem_31_2(): #Coin sums
    coins = [200,100,50,20,10,5,2,1]
    def findposs(money, maxcoin):
        sum = 0
        if (maxcoin == 7): return 1
        for i in range(maxcoin, 8):
            left = money - coins[i]
            if (left == 0): sum+=1
            if (left > 0): sum += findposs(left,i)
        return sum
    print(findposs(200,0))

def problem_31_3(): #Coin sums
    #http://www.algorithmist.com/index.php/Coin_Change
    #http://blog.dreamshire.com/2009/03/31/project-euler-problem-31-solution/
    #http://users.softlab.ece.ntua.gr/~ttsiod/euler31.html
    c = [1, 2, 5, 10, 20, 50, 100, 200]
    d = {x: [1] + [0] * 7 for x in range(1, 201)}
    for i in range(1, 201):
        for j in range(1, 8):
            if i == c[j]: d[i][j] = d[i][j-1] + 1
            elif i < c[j]: d[i][j] = d[i][j-1]
            else: d[i][j] = d[i][j-1] + d[i-c[j]][j]
    print(d[200][-1])

def problem_32():
    def sum2x3():
        s={1,2,3,4,5,6,7,8,9}
        m2={(x,y) for x in s for y in s if x != y}
        result = set()
        for x, y in m2:
            t = s - {x,y}
            m3={(a,b,c) for a in t for b in t for c in t if a != b and a != c and b!=c}
            for a,b,c in m3:
                u = t - {a,b,c}
                num = (10*x+y)*(100*a+10*b+c)
                v = [int(n) for n in str(num)]
                if (len(u) == len(v) and u == set(v)):
                    result.add(num)
                    print((10*x+y, 100*a+10*b+c, num))
        return sum(result)
    def sum1x4():
        s={1,2,3,4,5,6,7,8,9}
        result = set()
        for x in s:
            t = s - {x}
            m4={(a,b,c,d) for a in t for b in t for c in t  for d in t if a != b and a != c and b!=c and a!=d and b!=d and c!=d}
            for a,b,c,d in m4:
                u = t - {a,b,c,d}
                num = x*(1000*a + 100*b+10*c+d)
                v = [int(n) for n in str(num)]
                if (len(u) == len(v) and u == set(v)):
                    result.add(num)
                    print((x, 1000*a + 100*b+10*c+d, num))
        return sum(result)
    print(sum2x3()+sum1x4())

def problem_32_2():
    # The result is 4 bit, so it is 9876 at most in this case
    s = set()
    for x in range(1, 100):
        for y in range(100, 10000):
            if ''.join(sorted(str(x*y)+str(x)+str(y))) == '123456789':
                s.add(x*y)
    print(sum(s))

def problem_33():
    def bigDivider(m,n):
        k = m%n
        while(k!=0):
            m = n
            n = k
            k = m%n
        return n

    s = [(x,y) for x in range(1,10) for y in range(0,10)]
    t= []
    for x,y in s:
        for a,b in s:
            n = 10*x+y
            d = 10*a+b
            if (d <= n):  continue
            if (y == a and d*x==n*b):
                t.append((n,d))
            elif (x == b and d*y==n*a):
                t.append((n,d))

    nn,dd = 1,1
    for n,d in t:
        nn *= n
        dd *= d
    divider = bigDivider(nn,dd)
    print((nn,dd,divider))
    print(dd//divider)

def problem_34():
    def getN():
        n=1
        while(True):
            if (10**(n-1) > n*math.factorial(9)):
                return n
            n=n+1

    def digitFactorial(n):
        m = n
        sums = 0
        while(m != 0):
            k = m%10
            sums += math.factorial(k)
            m = m//10
        return sums == n

    maxdigits = getN()-1
    print(maxdigits)
    s=[n for n in range(10,maxdigits*math.factorial(9)) if digitFactorial(n)]
    print(sum(s))

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

def problem_36():
    def palindrome(n):
        digits = str(n)
        for i in range(len(digits)//2):
            if digits[i] != digits[-i-1]:
                return False
        digits = bin(n)[2:]
        for i in range(len(digits)//2):
            if digits[i] != digits[-i-1]:
                return False
        return True
    print(sum(n for n in range(10**6) if palindrome(n)))

def problem_36_2():
    print(sum([i for i in range(1,1000000) if str(i)==str(i)[::-1] if bin(i)[2:]==bin(i)[2:][::-1]]))

def problem_37():
    def prime(n):
        if (n<2):
            return False
        return all(n%x != 0 for x in range(2, int(n**0.5)+1))

    s=[]
    i = 10
    while(len(s) < 11):
        i += 1
        if not prime(i):
            continue

        if( all(prime(n) for n in [int(str(i)[j:]) for j in range(1, len(str(i)))]) and \
            all(prime(n) for n in [int(str(i)[:j]) for j in range(1, len(str(i)))])):
            s.append(i)
    
    print(s)
    print(sum(s))

def problem_38():
    def panMultiples3():
        for i in permutations('987654321'):
            n1 = int(''.join(i[0:4]))
            n2 = int(''.join(i[4:9]))
            if (n1*2 == n2):
                return int(''.join(i))

    def panMultiples2():
        for i in permutations('987654321'):
            n1 = int(''.join(i[0]))
            n2 = int(''.join(i[1:3]))
            n3 = int(''.join(i[3:5]))
            n4 = int(''.join(i[5:7]))
            n5 = int(''.join(i[7:9]))
            if (n1*2 == n2 and n1*3==n3 and n1*4==n4 and n1*5==n5):
                return int(''.join(i))

    def panMultiples():
        for i in permutations('987654321'):
            n1 = int(''.join(i[0:3]))
            n2 = int(''.join(i[3:6]))
            n3 = int(''.join(i[6:9]))
            if (n1*2 == n2 and n1*3==n3):
                return int(''.join(i))
    print(panMultiples3())

def problem_39():
    def rightTriangle(a,b,c):
        if (c <= b):
            return False
        return a*a + b*b == c*c

    def getSolution(p):
        s = [(a,b,p-a-b) for a in range(1,p//3) for b in range(a,p) if rightTriangle(a,b,p-a-b)]
        return len(s)

    s =[(getSolution(i), i) for i in range(1,1000) if getSolution(i) != 0]
    print( max(s))

def problem_39_2():
    s={}
    for a in range(1,333):
        for b in range(a,1000):
            cc = a*a+b*b
            c=int(cc**0.5)
            if (c*c == cc):
                p = a+b+c
                if (p<1000):
                    if (p not in s):
                        s[p] = 1
                    else:
                        s[p] += 1
    print(max(s.values()))

def problem_40():
    def digits(n): # The number of digits of the number n
        m = 0
        while(n != 0):
            n = n // 10
            m += 1
        return m

    def digit(n,i): # The i-th digit of the number n
        for k in range(i):
            n = n // 10
        return n%10

    def pos(po): # Get the digit from the po-th digit
        i = 0
        length = 0
        while(length < po):
            length += digits(i)
            i += 1
        return digit(i-1, length - po)

    #val = 1
    #for i in range(7):
    #    po = 10**i
    #    val *= pos(po)
    val = functools.reduce(lambda x,y: x*y, [pos(10**i) for i in range(7)])
    print(val)

def problem_40_2():
    d=''.join(map(str,range(1000000)))
    print(functools.reduce(operator.mul,[int(d[10**i]) for i in range(7)]))

def problem_41():
    def prime(n):
        if n < 2: return False
        return all(n%x != 0 for x in range(2, int(n**0.5)+1))

    def pandigital(n):
        s=[]
        while(n > 0):
            m = n % 10
            if (m == 0):
                return False
            s.append(m)
            n = n // 10
        s.sort()
        for i in range(len(s)):
            if(i+1 != s[i]):
                return False
        return True

    #Note: Nine numbers cannot be done (1+2+3+4+5+6+7+8+9=45 => always dividable by 3)
    #Note: Eight numbers cannot be done (1+2+3+4+5+6+7+8=36 => always dividable by 3)
    i = 7654321
    while(i > 2):
        if pandigital(i) and prime(i):
            print(i)
            return
        i -= 2

def problem_41_2(): #Faster than the previous solution
    def prime(n):
        if n < 2: return False
        return all(n%x != 0 for x in range(2, int(n**0.5)+1))

    for i in permutations('7654321'):
        n = int(''.join(i))
        if prime(n):
            print(n)
            return

def problem_42():
    def triangle(n):
        i = 1
        while(True):
            k = i*(i+1)//2
            if(k == n):
                return True
            elif(k > n):
                return False
            i += 1

    def getData(data):
        fp = open("problem42.txt","r")
        for line in fp:
            buff = line.split(",")
            data.extend([(lambda s:s.strip('"'))(x) for x in buff])

    #words =[]
    #getData(words)
    words = eval( '[' + open( 'problem42.txt' ).readlines()[ 0 ] + ']' )
    s = filter(lambda word: triangle(sum([ord(x) - 64 for x in word])), words)
    print(len(list(s)))

def problem_43():
    def subDivisility():
        s = []
        prime =[2,3,5,7,11,13,17]
        for i in permutations('9876543210'):
            if (all(int(''.join(i[j+1:j+4]))%prime[j] == 0 for j in range(7))):
                s.append(int(''.join(i)))
        return s

    print (sum(subDivisility()))
    
def problem_44(): # good problem
    def pentagonal(p):
        return ((((1 + 24*p) ** 0.5) + 1) / 6) % 1 == 0
    
    num= 10000
    s = [i*(3*i-1)//2 for i in range(1,num)]
    for i,a in enumerate(s):
        for b in s[i+1:]:
            if(pentagonal(b-a) and pentagonal(a+b)):
                print((a,b,b-a))
                return
    
def problem_45():
#    def pentagonal(n): 
#        k=1
#        i=1
#        while(k < n):
#            k=i*(3*i-1)//2
#            i+=1
#        return k==n
#    
#    def hexagonal(n):
#        k=1
#        i=1
#        while(k < n):
#            k=i*(2*i-1)
#            i+=1
#        return k==n
    
    def isPentagonal(p):
        return ((((1 + 24*p) ** 0.5) + 1) / 6) % 1 == 0
 
    def isHexagonal(h):
        return ((((1 + 8*h) ** 0.5) + 1) / 4) % 1 == 0
    
    i=286
    while(True):
        n=i*(i+1)//2
        if isPentagonal(n) and isHexagonal(n):
            print ((i,n))
            break
        i += 1

def problem_46():
    def prime(n):
        if (n<2):
            return False
        for x in range(2, int(n**0.5)+1):
            if n%x == 0: return False
        return True
    
    def conjercture(num):
        s=[x for x in range(1,num) if prime(x)]
        for i in range(9, s[-1], 2):
            for p in s:
                if (i-p == 0): # i is a prime
                    break
                if (i-p < 0):
                    return i   
                if (((i-p)/2)**0.5 % 1 == 0):
                    break
        return 0
     
    print(conjercture(10000))
    
def problem_46_2():
    def prime(n):
        if (n<2):
            return False
        for x in range(2, int(n**0.5)+1):
            if n%x == 0: return False
        return True
    
    def conjercture():
        s = []
        i = 1
        while(True):
            i += 1
            if(prime(i)):
                s.append(i)
                continue
            if (i % 2 == 0):
                continue

            bFound = False
            for p in s:
                if (((i-p)/2)**0.5 % 1 == 0):
                    bFound = True
                    break
                
            if not bFound:
                return i

    print(conjercture())

def problem_47():
    def prime(n):
        if (n<2):
            return False
        for x in range(2, int(n**0.5)+1):
            if n%x == 0: return False
        return True
    
    def factor(n):
        s=set()
        while(n != 0):
            i = 2
            while(i < n):
                if(n%i == 0):
                    s.add(i)
                    n = n // i
                    continue
                i += 1
            if (i==n):
                s.add(i)
                break

        return s
    
    i = 100
    while(True):
        if (len(factor(i)) != 4):
            i += 1
            continue
        if (len(factor(i+1)) != 4):
            i += 2
            continue
        if (len(factor(i+2)) != 4):
            i += 3
            continue
        if (len(factor(i+3)) != 4):
            i += 4
            continue
        print(i)
        break

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
    starttime = time.clock()
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
    #problem_28()
    #problem_29()
    #problem_30()
    #problem_31()
    #problem_31_2()
    #problem_31_3()
    #problem_32()
    #problem_32_2()
    #problem_33()
    #problem_34()
    #problem_35()
    #problem_36()
    #problem_36_2()
    #problem_37()
    #problem_38()
    #problem_39()
    #problem_39_2()
    #problem_40()
    #problem_40_2()
    #problem_41()
    #problem_41_2()
    #problem_42()
    #problem_43()
    #problem_44()
    #problem_45()
    #problem_46()
    #problem_46_2()
    problem_47()
    #problem_67()
    endtime = time.clock()
    print("It takes %f" % (endtime-starttime))