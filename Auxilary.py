import math

def numberOfLetters(num):
    d = dict()
    d[0] = ""
    d[1] = "one"
    d[2] = "two"
    d[3] = "three"
    d[4] = "four"
    d[5] = "five"
    d[6] = "six"
    d[7] = "seven"
    d[8] = "eight"
    d[9] = "nine"
    d[10] = "ten"
    d[11] = "eleven"
    d[12] = "twelve"
    d[13] = "thirteen"
    d[14] = "fourteen"
    d[15] = "fifteen"
    d[16] = "sixteen"
    d[17] = "seventeen"
    d[18] = "eighteen"
    d[19] = "nineteen"
    d[20] = "twenty"
    d[30] = "thirty"
    d[40] = "forty"
    d[50] = "fifty"
    d[60] = "sixty"
    d[70] = "seventy"
    d[80] = "eighty"
    d[90] = "ninety"
    d[100] = "hundred"

    if len(str(num)) == 1:
        return len(d[num])
    if len(str(num)) == 2:
        if num < 20:
            return len(d[num])
        else:
            return len(d[num - (num % 10)] + d[num % 10])
    if len(str(num)) == 3:
        strLen = len(d[int(num/100)]) + len(d[100])
        if num % 100 != 0:
            strLen += len("and") + numberOfLetters(num % 100)
        return strLen
    return len("onethousand")


def findChainLength(num):
    if num == 1:
        return 1
    if num % 2 == 0:
        num = num / 2
    else:
        num = 3*num + 1
    return 1 + findChainLength(num)


def numDivisor(num):
    cnt = 1
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            cnt += 2
    return cnt


def isPolindrome(num):
    strNum = list(str(num))
    a = ''.join(strNum[:])
    b = ''.join(strNum[::-1])
    if a==b:
        return True
    else:
        return False


def isPrime(num):
    """checks if number is prime, expects to get numbers greater than 2"""
    if num == 2:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)) + 1), 2):
        if num % i == 0:
            return False
    return True


def isabundant(num):
    if sum(divisors(num)) > num:
        return True
    return False


def divisors(num):
    divs = list()
    divs.append(1)
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.append(i)
            if i != num / i:
                divs.append(num / i)
    return divs


def count(S, m, n):
    table = [[0 for x in range(m)] for x in range(n + 1)]

    # Fill the enteries for 0 value case (n = 0)
    for i in range(m):
        table[0][i] = 1

    # Fill rest of the table enteries in bottom up manner
    for i in range(1, n + 1):
        for j in range(m):
            # Count of solutions including S[j]
            x = table[i - S[j]][j] if i - S[j] >= 0 else 0

            # Count of solutions excluding S[j]
            y = table[i][j - 1] if j >= 1 else 0

            # total count
            table[i][j] = x + y

    return table[n][m - 1]


def isPandigital(num):
    digs = [int(x) for x in str(num)]
    if len(digs) == len(set(digs)) == max(digs) and min(digs) == 1:
        return True
    return False


def wordValue(word):
    sumWord = 0
    for ch in word:
        sumWord += ord(ch.upper()) - ord('A') + 1
    return sumWord


def trianNum(n):
    return n * (n + 1) // 2


def isPentagonal(num):
    penTest = (math.sqrt(1 + 24 * num) + 1.0) / 6.0;
    return penTest == int(penTest);


def primeListInRange(start=1,end=100):
    retList = list()
    for i in range(start,end):
        if isPrime(i):
            retList.append(i)
    return retList


def distinctPrimeFactors(num,primeList = None):
    primeFactors = set()
    if primeList is None:
        primes = primeListInRange(2, num+1)
    else:
        primes = primeList
    cnt = 0
    while num > 1:
        if num % primes[cnt] == 0:
            primeFactors.add(primes[cnt])
            num = num // primes[cnt]
        else:
            cnt += 1
    return list(primeFactors)


def main():
    pass

if __name__ == "__main__":
    main()