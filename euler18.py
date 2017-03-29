import math
import datetime
from dateutil.relativedelta import relativedelta


def euler18():
    dicLines = {0 : [75],
                1 : [95, 64],
                2 : [17, 47, 82],
                3 : [18, 35, 87, 10],
                4 : [20, 4, 82, 47, 65],
                5 : [19, 1, 23, 75, 3, 34],
                6 : [88, 2, 77, 73, 7, 63, 67],
                7 : [99, 65, 4, 28, 6, 16, 70, 92],
                8 : [41, 41, 26, 56, 83, 40, 80, 70, 33],
                9 : [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                10 : [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                11 : [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                12 : [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                13 : [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                14 : [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]}

    for i in range(14,0,-1):
        for j in range(len(dicLines[i])-1):
            dicLines[i-1][j] = max(dicLines[i-1][j] + dicLines[i][j], dicLines[i-1][j] + dicLines[i][j+1])
    print dicLines[0]


def euler19():
    cnt = 0
    startDate = datetime.datetime.strptime('01-01-1901', '%d-%m-%Y')
    endDate = datetime.datetime.strptime('01-01-2001', '%d-%m-%Y')
    numMonths = relativedelta(endDate,startDate).years * 12

    for i in range(numMonths):
        if startDate.weekday() == 6:
            cnt += 1
        startDate = startDate + relativedelta(months=1)
    print cnt


def euler20():
    n = 100
    fact = math.factorial(n)
    digits = [int(d) for d in str(int(fact))]

    print sum(digits)


def euler21():
    amics = list()
    for i in range(10000):
        if i in amics:
            pass
        else:
            divs = sum(divisors(i))
            if i == sum(divisors(divs)) and i != divs:
                amics.append(i)
                amics.append(divs)
    print amics
    print sum(amics)


def divisors(num):
    divs = list()
    divs.append(1)
    for i in range(2,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.append(i)
            divs.append(num / i)
    return divs


def main():
    #euler18()
    #euler19()
    #euler20()
    euler21()

if __name__ == "__main__":
    main()