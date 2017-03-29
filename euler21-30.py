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


def main():
    euler21()


if __name__ == "__main__":
    main()
