import Auxilary as aux
import fractions
import math



def euler31():
    coins = [1,2,5,10,20,50,100,200]
    m = len(coins)
    n = 200
    print "Number of different ways can 2pounds be made using any number of coins is: " + str(aux.count(coins, m, n))


def euler32():
    resSet = set()

    for i in range(2,10):
        for j in range(1000,10000):
            res = i*j
            if aux.isPandigital(int(str(res) + str(i) + str(j))):
                resSet.add(res)

    for i in range(10,100):
        for j in range(100,1000):
            res = i * j
            if aux.isPandigital(int(str(res) + str(i) + str(j))):
                resSet.add(res)
    print "The sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital is: " + str(sum(resSet))

def euler33():
    prod = fractions.Fraction(1,1)
    for i in range(10,99):
        for j in range(10,i):
            init = fractions.Fraction(j, i)
            a = j / 10
            b = j % 10
            c = i / 10
            d = i % 10
            if a == c and d != 0:
                if fractions.Fraction(b, d) == init:
                    prod *= init
            elif a == d and c != 0:
                if fractions.Fraction(b, c) == init:
                    prod *= init
            elif b == c and d != 0:
                if fractions.Fraction(a, d) == init:
                    prod *= init
            elif b == d and b != 0:
                if fractions.Fraction(a,c) == init:
                    prod *= init
    print "lowest common denom is: " + str(prod)

def euler34():
    globalSum = 0
    for i in range(3,2500000):
        s = 0
        s = sum([math.factorial(int(x)) for x in str(i)])
        if s == i:
            print i, s
            globalSum += s
    print "sum is: " + str(globalSum)

def euler35():
    cnt = 0
    primeList = list()
    for i in range(2,1000000):
        if aux.isPrime(i):
            primeList.append(i)
    print len(primeList)
    for i in primeList:
        j=0
        stillPrime = True
        digitList = [int(x) for x in str(i)]
        listLen = len(digitList)
        while (j < listLen - 1):
            j += 1
            if aux.isPrime(int("".join(str(x) for x in digitList[j:]) + "".join(str(x) for x in digitList[:j]))) is not True:
                stillPrime = False
                break
        if stillPrime:
            print i
            cnt += 1
    print cnt+1

def euler36():
    s = 0
    for i in range(1000000):
        if aux.isPolindrome(i) and aux.isPolindrome(int(bin(i)[2:])):
            s += i
    print "sum of all polindromic numbers in both bases is: " + str(s)

def euler39():
    maxi = -1
    maxiNum = 0
    num = 1000
    for p in range(num):
        cnt = 0
        for i in range(1,p):
            j = i + 1
            k = p - 1
            while j < k:
                if i + j + k == p:
                    if i**2 + j**2 == k**2:
                        cnt += 1
                    j += 1
                elif i + j + k < p:
                    j += 1
                else:
                    k -= 1

        if cnt > maxi:
            maxiNum = p
            maxi = cnt
    print "For which value of p <= 1000, is the number of solutions maximised: " + str(maxiNum)


def euler40():
    s = ""
    i = 1
    while len(s) < 1000000:
        s += str(i)
        i += 1
    print s[0], s[9], s[99], s[999], s[9999], s[99999], s[999999]
    print int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999])

def main():
    #euler31()
    #euler32()
    #euler33()
    #euler34()
    #euler35()
    #euler36()
    euler39()
    #euler40()


if __name__ == "__main__":
    main()
