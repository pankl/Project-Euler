import Auxilary as aux
from itertools import permutations

def euler21():
    amics = list()
    for i in range(10000):
        if i in amics:
            pass
        else:
            divs = sum(aux.divisors(i))
            if i == sum(aux.divisors(divs)) and i != divs:
                amics.append(i)
                amics.append(divs)
    print "The sum of all the amicable numbers under 10000 is: " + str(sum(amics))


def euler22():
    filename = "p022_names.txt"
    with open(filename, 'r') as infile:
        lines = infile.readline()
    linesSplit = lines.split(',')
    linesSplit.sort()
    totalScore = 0
    for ind, line in enumerate(linesSplit, start=1):
        sline = 0
        sline += sum([ord(ch) - ord('A') + 1 for ch in line if ch.isalpha()])
        totalScore += sline * ind
    print "The total of all the name scores in the file is: " + str(totalScore)


def euler23():
    lim, s = 28123, 0
    abundant = set()

    for n in range(1, lim + 1):
        if sum(aux.divisors(n)) > n:
            abundant.add(n)
        if not any((n - a in abundant) for a in abundant):
            s += n
    print "Sum of all the positive integers which cannot be written as the sum of two abundant numbers is: " + str(s)


def euler24():
    seed = [0,1,2,3,4,5,6,7,8,9]
    perms = permutations(seed)
    per = [x for x in perms][999999]
    print "The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is: " + ''.join(str(x) for x in per)

def euler25():
    hi,low = 1,1
    cnt=2
    while len(str(hi)) < 1000:
        cnt+=1
        hi = hi + low
        low = hi - low
    print "First term in the Fibonacci sequence to contain 1000 digits is: " + str(cnt)


def euler26():
    maxLen = 0
    num = 0
    for i in range(1000, 2, -1):
        rems = list()
        rem = 1 % i
        while rem != 0 and rem not in rems:
            rems.append(rem)
            rem *= 10
            rem %= i
        if len(rems) > maxLen:
            maxLen = len(rems)
            num = i

    print "Max len is: " + str(maxLen)
    print "Belongs to number: " + str(num)

def euler27()
def main():
    #euler21()
    #euler22()
    #euler23()
    #euler24()
    #euler25()
    euler26()


if __name__ == "__main__":
    main()
