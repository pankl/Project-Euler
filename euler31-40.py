import Auxilary as aux


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


def main():
    #euler31()
    euler32()


if __name__ == "__main__":
    main()
