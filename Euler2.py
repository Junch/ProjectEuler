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

if __name__ == '__main__':
    unittest.main()

class problem_57(unittest.TestCase):
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