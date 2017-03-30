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
    if num % 2 == 0:
        return False
    for i in range(3, int(math.ceil(math.sqrt(num)) + 1), 2):
        if num % i == 0:
            return False
    return True


def isabundant(num):
    if sum(divisors(num)) + 1 > num:
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


def main():
    pass

if __name__ == "__main__":
    main()