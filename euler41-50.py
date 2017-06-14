import Auxilary as aux
import math
import itertools


def euler41():
    n = 10
    found = False
    while not found:
        perms = itertools.permutations(range(1, n))
        nums = list()
        for p in perms:
            nums.append(reduce(lambda rst, d: rst * 10 + d, (p)))
        nums.sort(reverse=True)
        for num in nums:
            if aux.isPrime(num):
                found = True
                print num
                break
        n -= 1


def euler42():
    with open("p042_words.txt") as f:
        words = f.readlines()
        f.close()
    words = words[0].replace('"','').split(',')
    cnt = 0
    for w in words:
        for i in range(20):
            if aux.wordValue(w) == aux.trianNum(i):
                cnt += 1
    print cnt


def euler43():
    n = 10
    mySum = 0
    perms = itertools.permutations(range(0, n))
    for p in perms:
        nump = int(''.join(map(str,list(p))))
        if (int(str(nump)[1:4]) % 2 == 0 and
            int(str(nump)[2:5]) % 3 == 0 and
            int(str(nump)[3:6]) % 5 == 0 and
            int(str(nump)[4:7]) % 7 == 0 and
            int(str(nump)[5:8]) % 11 == 0 and
            int(str(nump)[6:9]) % 13 == 0 and
            int(str(nump)[7:]) % 17 == 0):
            mySum += nump
    print mySum

def euler44():
    found = False
    i = 1
    while not found:
        i += 1
        n = i * (3 * i - 1) / 2;
        for j in range(i-1, 0, -1):
            m = j * (3 * j - 1) / 2
            if aux.isPentagonal(n - m) and aux.isPentagonal(n + m):
                result = n-m
                found = True
                break
    print result

def euler45():
    i = 143
    found = False
    while not found:
        i+=1
        if aux.isPentagonal(i*(2*i-1)):
            found = True
            res = i * (2*i-1)
    print res

def euler46():
    n = 1000000
    primes = aux.primeListInRange(1,n+1)
    for i in range(3,n,2):
        found = False
        cnt = 0
        if i in primes:
            pass
        else:
            while not found and primes[cnt] < i:
                if math.sqrt((i - primes[cnt]) / 2) == math.floor(math.sqrt((i - primes[cnt]) / 2)):
                    found = True
                    #print i, primes[cnt], (i - primes[cnt]) / 2, math.floor(math.sqrt((i - primes[cnt]) / 2))
                else:
                    cnt+=1
            if not found:
                print "hip hip found it", i


def euler47():
    target = 4
    foundSoFar = 0
    num = 210
    primeList = aux.primeListInRange(1,1000000)
    while foundSoFar < target:
        num += 1
        if (len(aux.distinctPrimeFactors(num,primeList)) >= 4):
            foundSoFar += 1
        else:
            foundSoFar = 0
    print num - 3

def euler48():
    res = 0
    for i in range(1,1001):
        res += i**i
    print str(res)[-10:]

def euler49():
    primeList = aux.primeListInRange(1000,10000)
    for n in primeList:
        a = n + 3330
        b = n + 6660
        if aux.isPrime(a) and aux.isPrime(b):
            if len(str(a)) < 5 and len(str(b)) < 5:
                digsN = [int(x) for x in str(n)]
                digsA = [int(x) for x in str(a)]
                digsB = [int(x) for x in str(b)]
                digsA.sort(), digsB.sort(), digsN.sort()
                #print digsB, digsN
                if digsN == digsA:
                    print n,a,b

def euler50():
    primes = aux.primeListInRange(1,3940)
    sumPrimes = sum(primes)

    found = False
    i = 0
    while not found:
        print sumPrimes
        if sumPrimes < 1000000 and aux.isPrime(sumPrimes):
            print 'done'
            print sumPrimes ,i
            found = True
            break
        sumPrimes -= primes[i]
        i += 1


def main():
    #euler41()
    #euler42()
    #euler43()
    #euler44()
    #euler45()
    euler46()
    #euler47()
    #euler48()
    #euler49()
    #euler50()

if __name__=='__main__':
    main()
