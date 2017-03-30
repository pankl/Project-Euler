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
    print amics
    print sum(amics)


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
    print totalScore


def main():
    #euler21()
    euler22()


if __name__ == "__main__":
    main()
