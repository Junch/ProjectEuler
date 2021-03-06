import math
import unittest

def problem_53():
    def combinatatoric(n,r):
        return math.factorial(n)//math.factorial(n-r)//math.factorial(r)

    count = 0
    for n in range(1,101):
        for r in range(0,n+1):
            v = combinatatoric(n,r)
            if (v > 10**6):
                count += 1
    print(count)


'''
High Card:       0
One Pair:        1
Two Pair:        2
Three of a kind: 3
Straight:        4
Flush:           5
Full house:      6
Four of a kind:  7
Straight Flush:  8
'''

class Hand(object):
    def __init__(self, v):
        self.val = v
        self.val.sort(reverse=True)

    def straight(self):
        for i in range(1,5):
            if self.val[i-1][0] - 1 != self.val[i][0]:
                return False
        return True

    def flush(self):
        return all(x[1] == self.val[0][1] for x in self.val)

    def samekind(self):
        nums = [x[0] for x in self.val]
        values = set([(nums.count(x), x) for x in nums if nums.count(x) > 1])
        return values

    def cal(self):
        bStraight = self.straight()
        bFlush    = self.flush()
        if(bStraight and bFlush):
            return (8, self.val[0][0])
        if(bStraight):
            return (4, self.val[0][0])
        if(bFlush):
            ret = (5, self.val[0][0], self.val[1][0],\
                      self.val[2][0], self.val[3][0], self.val[4][0])
            return ret
        kind = [x for x in self.samekind()]
        length = len(kind)
        if length == 0:
            ret = (0, self.val[0][0], self.val[1][0],\
                      self.val[2][0], self.val[3][0], self.val[4][0])
            return ret
        elif length == 1:
            key = kind[0][1]
            if kind[0][0] == 4:
                return (7, key)
            elif kind[0][0] == 3:
                return (3, key)
            elif kind[0][0] == 2:
                s = [x[0] for x in self.val if x[0] != key]
                ret = (1,key,s[0],s[1],s[2])
                return ret
        elif length == 2:
            if (kind[0][0] == 3):
                return (6, kind[0][1])
            elif(kind[1][0] == 3):
                return (2, kind[1][1])
            else:
                maxv = max(kind[0][1], kind[1][1])
                minv = min(kind[0][1], kind[1][1])
                s = [x[0] for x in self.val if x[0]!=minv and x[0]!=maxv]
                return (2, maxv, minv, s[0])

def problem_54():
    def number(c):
        if c <= '9' and c >= '0':
            return int(c)
        if c == 'T':
            return 10
        if c == 'J':
            return 11
        if c == 'Q':
            return 12
        if c == 'K':
            return 13
        if c == 'A':
            return 14

    count=0
    fp = open("problem54.txt", "r")
    for line in fp:
        line = line.rstrip()
        s = [x for x in line.split()]
        a = [(number(x[0]),x[1]) for x in s[0:5]]
        b = [(number(x[0]),x[1]) for x in s[5:10]]
        hand1 = Hand(a)
        hand2 = Hand(b)
        if hand1.cal() > hand2.cal():
            count += 1
    print(count)

def problem_55():
    def palindromic(n):
        a=[x for x in str(n)]
        length = len(a)
        return all(a[i]==a[length-i-1] for i in range(length//2))

    def reverse(n):
        a=[int(x) for x in str(n)]
        m = 0
        for i in a[::-1]:
            m = 10*m + i
        return m

    def lychrel(n):
        for iterations in range(50):
            a = n + reverse(n)
            if (palindromic(a)):
                return False
            else:
                n = a
        return True

    print(len([x for x in range(1,10000) if lychrel(x)]))

def problem_56():
    maxv = 0
    for a in range(1,101):
        if a % 10 == 0:
            continue
        for b in range(1,101):
            sums = sum([int(x) for x in str(a**b)])
            if maxv < sums:
                maxv = sums
    print(maxv)

def problem_57():
    d = 2
    n = 3
    c = 0
    for i in range(1000):
        if len(str(d)) < len(str(n)):
            c += 1
        d, n = d+n, n+2*d
    print (c)

def problem_59():
    fp = open("problem59.txt","r")
    data = []
    for line in fp:
        line = line.split(',')
        a = [int(x) for x in line]
        data.extend(a)

    s = [x for x in range(ord('a'), ord('z')+1)]

    def decrypt():
        for i in s:
            for j in s:
                for k in s:
                    result = []
                    for m, d in enumerate(data):
                        if m % 3 == 0:
                            result.append(chr(i ^ d))
                        elif m % 3 == 1:
                            result.append(chr(j ^ d))
                        else:
                            result.append(chr(k ^ d))
                    msg = ''.join(result)
                    num = msg.count(" the ")
                    if (num > 1):
                        print (msg)
                        ret = sum([ord(x) for x in msg])
                        print (ret)
                        return
    decrypt()


def problem_60():
    def prime(n):
        if (n < 2):
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0: return False
        return True

    def pair(m, n):
        a = ''.join(str(m))
        b = ''.join(str(n))

        if not prime(int(a + b)):
            return False
        return prime(int(b + a))

    def maxpath(key, primedict):
        result=[[key]]
        last=[]
        while len(result) > 0:
            x = result.pop(0)
            xx = x[-1]

            last = list(x) #it is to copy the x

            if xx not in primedict.keys():
                continue

            for y in primedict[xx]:
                bothPrime = True
                for i in x:
                    maxone = max(y,i)
                    minone = min(y,i)
                    if minone not in primedict[maxone]:
                        bothPrime = False
                        break
                if (bothPrime):
                    z = list(x)
                    z.append(y)
                    result.append(z)

        return last

    limit = 10000
    bolprimelist = [True] * limit
    primelist = []
    for i in range(2, limit):
        if bolprimelist[i]:
            primelist.append(i)
            for j in range(i*i, limit, i):
                bolprimelist[j] = False

    primedict={}
    for i, x in enumerate(primelist):
        for y in primelist[0:i-1]:
             if pair(x,y):
                if x in primedict.keys():
                    primedict[x].append(y)
                else:
                    primedict[x] = [y]
    
    minvalue = 10**6
    value = []
    for x in primedict.keys():
        s = maxpath(x, primedict)
        if (len(s) == 5):
            sums = sum(s)
            if (sums < minvalue):
                minvalue = sums
                value = list(s)
    print(minvalue)
    print(value)
 
def problem_60_2():
    def prime(n):
        if (n < 2):
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0: return False
        return True

    def pair(m, n):
        a = ''.join(str(m))
        b = ''.join(str(n))

        if not prime(int(a + b)):
            return False
        return prime(int(b + a))

    limit = 10000
    bolprimelist = [True] * limit
    primelist = []
    for i in range(2, limit):
        if bolprimelist[i]:
            primelist.append(i)
            for j in range(i*i, limit, i):
                bolprimelist[j] = False

    def getsums():
        for i, a in enumerate(primelist):
            for j, b in enumerate(primelist[i+1:]):
                if not pair(a,b): continue
                for k, c in enumerate(primelist[i+j+2:]):
                    if not pair(a,c) or not pair(b,c): continue
                    for l, d in enumerate(primelist[i+j+k+3:]):
                        if not pair(a,d) or not pair(b,d) or not pair(c,d): continue
                        for e in primelist[i+j+k+l+4:]:
                            if pair(a,e) and pair(b,e) and pair(c,e) and pair(d,e):
                                value = sum([a,b,c,d,e])
                                return value
    print(getsums())

def problem_65():
    def numbers(n):
        s = [2, 1]
        i = 0
        while(len(s) < n+1):
            i += 1
            s.append(i*2)
            s.append(1)
            s.append(1)

        while(len(s) > n+1):
            s.pop()
        return s

    def add(num, m):
        n, d=num[0], num[1]
        return (n*m + d, n)

    n = 99
    s = numbers(n)
    s.reverse()

    value = (s[0],1)
    for i in s[1:]:
        value = add(value, i)

    print(sum([int(x) for x in str(value[0])]))

if __name__ == '__main__':
    unittest.main()

class problem_54(unittest.TestCase):
    def test_straight(self):
        hand = Hand([(2,'H'),(3,'C'), (4,'A'), (5,'S'),(6,'D')])
        self.assertTrue(hand.straight())
        hand = Hand([(4,'H'),(3,'C'), (2,'A'), (6,'S'),(5,'D')])
        self.assertTrue(hand.straight())
        hand = Hand([(2,'H'),(3,'C'), (4,'A'), (5,'S'),(7,'D')])
        self.assertFalse(hand.straight())

    def test_flush(self):
        hand = Hand([(2,'H'),(3,'H'), (4,'H'), (5,'H'),(6,'H')])
        self.assertTrue(hand.flush())
        hand = Hand([(2,'H'),(3,'H'), (4,'H'), (5,'S'),(6,'H')])
        self.assertFalse(hand.flush())

    def test_samekind(self):
        hand = Hand([(2,'H'),(3,'C'), (4,'A'), (5,'S'),(6,'D')])
        self.assertEqual(set(), hand.samekind())
        hand = Hand([(2,'H'),(3,'C'), (3,'A'), (5,'S'),(6,'D')])
        self.assertEqual(set([(2,3)]), hand.samekind())
        hand = Hand([(2,'H'),(3,'C'), (3,'A'), (3,'S'),(3,'D')])
        self.assertEqual(set([(4,3)]), hand.samekind())
        hand = Hand([(3,'H'),(3,'C'), (4,'A'), (4,'S'),(4,'D')])
        self.assertEqual(set([(3,4),(2,3)]), hand.samekind())

    def test_cal(self):
        #high card
        hand0 = Hand([(2,'H'),(4,'C'), (5,'A'), (7,'S'),(9,'D')])
        self.assertEqual((0, 9, 7, 5, 4, 2), hand0.cal())
        #One pair
        hand1 = Hand([(2,'H'),(4,'C'), (4,'A'), (7,'S'),(9,'D')])
        self.assertEqual((1, 4, 9, 7, 2), hand1.cal())
        #Two pair
        hand2 = Hand([(7,'H'),(4,'C'), (4,'A'), (7,'S'),(9,'D')])
        self.assertEqual((2, 7, 4, 9), hand2.cal())
        #three of a kind
        hand3 = Hand([(2,'H'),(4,'C'), (4,'A'), (4,'S'),(9,'D')])
        self.assertEqual((3, 4), hand3.cal())
        #straight
        hand4 = Hand([(2,'H'),(3,'C'), (4,'A'), (5,'S'),(6,'D')])
        self.assertEqual((4, 6), hand4.cal())
        #flush
        hand5 = Hand([(2,'H'),(3,'H'), (4,'H'), (5,'H'),(7,'H')])
        self.assertEqual((5,7,5,4,3,2), hand5.cal())
        #full house
        hand6 = Hand([(10,'H'),(4,'C'), (4,'A'), (4,'S'),(10,'D')])
        self.assertEqual((6, 4), hand6.cal())
        #four of a kind
        hand7 = Hand([(10,'H'),(4,'C'), (4,'A'), (4,'S'),(4,'D')])
        self.assertEqual((7, 4), hand7.cal())
        #straight flush
        hand8 = Hand([(2,'S'),(3,'S'), (4,'S'), (5,'S'),(6,'S')])
        self.assertEqual((8, 6), hand8.cal())

        self.assertTrue(hand8.cal() > hand7.cal())