import Auxilary as aux


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


def main():
    euler21()
    euler22()
    euler23()


if __name__ == "__main__":
    main()
