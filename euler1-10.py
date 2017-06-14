import time
import math
import numpy as np
import Auxilary as aux


def euler1():
    s = 0
    for i in range(3,1000,3):
        s+=i
    for i in range(5,1000,5):
        if i % 3 != 0:
            s+=i
    print s


def euler2():
    low = 1
    hi = 2
    sum = 0
    while hi < 4000000:
        if hi % 2 == 0:
            sum += hi
        hi = hi + low
        low = hi - low
    print "Sum of the even-valued terms in Fib series under 4,000,000 is: " + str(sum)


def euler3():
    n = 600851475143
    divs = list()
    for i in range(int(math.sqrt(n))+1, 3, -2):
        if n % i == 0:
            divs.append(i)
            divs.append(int(n / i))
    divs.sort(reverse=True)
    for elem in divs:
        if aux.isPrime(elem):
            print "largest prime factor of the number 600851475143 is: " + str(elem)
            return


def euler4():
    i = 100
    j = 999
    polins = list()
    for i in range(100,999):
        for j in range(100,999):
            if aux.isPolindrome(i*j):
                polins.append(i*j)
    polins.sort(reverse=True)
    print polins
    print "The largest palindrome made from the product of two 3-digit numbers is: " + str(polins[0])


def euler5():
    prod = 1
    for i in (2,3,5,7,11,13,17,19):
        prod *= i
    prod *= 3
    prod *= 8
    print "Smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: " + str(prod)

def euler6():
    s = 0
    n = 101
    for i in range(1,n):
        s+= i**2
    print "The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is: " + str((n*(n-1)/2)**2 - s)


def euler7():
    cnt = 1
    i = 3
    while cnt <= 10001:
        if (aux.isPrime(i)):
            last = i
            cnt += 1
        i += 2
    print "The 10,001st prime number is: " + str(last)


def euler8():
    strNum = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843" \
             "8586156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557" \
             "6689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749" \
             "3035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776" \
             "6572733300105336788122023542180975125454059475224352584907711670556013604839586446706324415722155397" \
             "5369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474" \
             "8216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586" \
             "1786645835912456652947654568284891288314260769004224219022671055626321111109370544217506941658960408" \
             "0719840385096245544436298123098787992724428490918884580156166097919133875499200524063689912560717606" \
             "0588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    lstNum = list(strNum)
    maxProd = 0
    ind = -1
    for i in range(0,988):
        prod = 1
        for j in range(0,13):
            prod *= int(lstNum[i+j])
        if prod > maxProd:
            maxProd = prod
            ind = i
    print "Value of this product is: " + str(maxProd)
    print "Start index of it is: " + str(ind)

def euler9():
    for i in range(1,1000):
        for j in range(1,1000):
            if (i+j < 1000) and (i**2+j**2 == (1000 - (i+j))**2):
                print "The product of Pythagorean triplet for which a + b + c = 1000 is: " + str(i*j*(1000 - (i+j)))
                return


def euler10():
    start = time.time()
    mySum = 2
    for i in range(3,2000000,2):
        mySum = mySum + i if aux.isPrime(i) else mySum
    end = time.time()
    print "The sum of all the primes below two million is: " + str(mySum)
    print end - start


def main():
    euler1()
    euler2()
    euler3()
    euler4()
    euler5()
    euler6()
    euler7()
    euler8()
    euler9()
    euler10()

if __name__ == "__main__":
    main()
