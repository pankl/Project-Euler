import Auxilary as aux


def euler31():
    coins = [1,2,5,10,20,50,100,200]
    m = len(coins)
    n = 200
    print "Number of different ways can 2pounds be made using any number of coins is: " + str(aux.count(coins, m, n))


def main():
    euler31()


if __name__ == "__main__":
    main()
