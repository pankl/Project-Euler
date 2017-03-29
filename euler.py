import time
import math
import numpy as np


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
    for i in range(int(math.sqrt(n))+1,3,-2):
        if n % i == 0:
            divs.append(i)
            divs.append(int(n / i))
    divs.sort(reverse=True)
    for elem in divs:
        if isPrime(elem):
            print "largest prime factor of the number 600851475143 is: " + str(elem)
            return


def euler4():
    i = 100
    j = 999
    polins = list()
    for i in range(100,999):
        for j in range(100,999):
            if isPolindrome(i*j):
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
        if (isPrime(i)):
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
        mySum = mySum + i if isPrime(i) else mySum
    end = time.time()
    print "The sum of all the primes below two million is: " + str(mySum)
    print end - start

def euler11():

    arr = [ 8,2,22,97,38,15,0,40,0,75,4,5,7,78,52,12,50,77,91,8,
            49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48,4,56,62,0,
            81,49,31,73,55,79,14,29,93,71,40,67,53,88,30,3,49,13,36,65,
            52,70,95,23,4,60,11,42,69,24,68,56,1,32,56,71,37,2,36,91,
            22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80,
            24,47,32,60,99,3,45,2,44,75,33,53,78,36,84,20,35,17,12,50,
            32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70,
            67,26,20,68,2,62,12,20,95,63,94,39,63,8,40,91,66,49,94,21,
            24,55,58,5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72,
            21,36,23,9,75,0,76,44,20,45,35,14,0,61,33,97,34,31,33,95,
            78,17,53,28,22,75,31,67,15,94,3,80,4,62,16,14,9,53,56,92,
            16,39,5,42,96,35,31,47,55,58,88,24,0,17,54,24,36,29,85,57,
            86,56,0,48,35,71,89,7,5,44,44,37,44,60,21,58,51,54,17,58,
            19,80,81,68,5,94,47,69,28,73,92,13,86,52,17,77,4,89,55,40,
            4,52,8,83,97,35,99,16,7,97,57,32,16,26,26,79,33,27,98,66,
            88,36,68,87,57,62,20,72,3,46,33,67,46,55,12,32,63,93,53,69,
            4,42,16,73,38,25,39,11,24,94,72,18,8,46,29,32,40,62,76,36,
            20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74,4,36,16,
            20,73,35,29,78,31,90,1,74,31,49,71,48,86,81,16,23,57,5,54,
            1,70,54,71,83,51,54,69,16,92,33,48,61,43,52,1,89,19,67,48]

    asd = (np.asarray(arr)).reshape(20, 20)
    max_prod = 0

    for i in range(0,20):
        for j in range(0,20):
            #first we look right
            if j+3<20:
                temp_prod = asd.item((i,j))*asd.item((i,j+1))*asd.item((i,j+2))*asd.item((i,j+3))
                max_prod = temp_prod if temp_prod > max_prod else max_prod
            #now look down
            if i+3<20:
                temp_prod = asd.item((i, j)) * asd.item((i+1, j)) * asd.item((i+2, j)) * asd.item((i+3, j))
                max_prod = temp_prod if temp_prod > max_prod else max_prod
            #now look diagonal right
            if (i+3 < 20) and (j+3<20):
                temp_prod = asd.item((i, j)) * asd.item((i + 1, j + 1)) * asd.item((i + 2, j + 2)) * asd.item((i + 3, j + 3))
                max_prod = temp_prod if temp_prod > max_prod else max_prod
            #now look diagonal left
            if (i +3 < 20) and (j > 3):
                temp_prod = asd.item((i, j)) * asd.item((i + 1, j - 1)) * asd.item((i + 2, j - 2)) * asd.item((i + 3, j - 3))
                max_prod = temp_prod if temp_prod > max_prod else max_prod
    print "The greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20*20 grid is: " + str(max_prod)

def euler12():
    for i in range(10000,1000000):
        triag = i * (i+1) / 2
        if numDivisor(triag) > 500:
            print i
            print triag
            return


def euler13():
    arr = [37107287533902102798797998220837590246510135740250, 46376937677490009712648124896970078050417018260538,
           74324986199524741059474233309513058123726617309629, 91942213363574161572522430563301811072406154908250,
           23067588207539346171171980310421047513778063246676, 89261670696623633820136378418383684178734361726757,
           28112879812849979408065481931592621691275889832738, 44274228917432520321923589422876796487670272189318,
           47451445736001306439091167216856844588711603153276, 70386486105843025439939619828917593665686757934951,
           62176457141856560629502157223196586755079324193331, 64906352462741904929101432445813822663347944758178,
           92575867718337217661963751590579239728245598838407, 58203565325359399008402633568948830189458628227828,
           80181199384826282014278194139940567587151170094390, 35398664372827112653829987240784473053190104293586,
           86515506006295864861532075273371959191420517255829, 71693888707715466499115593487603532921714970056938,
           54370070576826684624621495650076471787294438377604, 53282654108756828443191190634694037855217779295145,
           36123272525000296071075082563815656710885258350721, 45876576172410976447339110607218265236877223636045,
           17423706905851860660448207621209813287860733969412, 81142660418086830619328460811191061556940512689692,
           51934325451728388641918047049293215058642563049483, 62467221648435076201727918039944693004732956340691,
           15732444386908125794514089057706229429197107928209, 55037687525678773091862540744969844508330393682126,
           18336384825330154686196124348767681297534375946515, 80386287592878490201521685554828717201219257766954,
           78182833757993103614740356856449095527097864797581, 16726320100436897842553539920931837441497806860984,
           48403098129077791799088218795327364475675590848030, 87086987551392711854517078544161852424320693150332,
           59959406895756536782107074926966537676326235447210, 69793950679652694742597709739166693763042633987085,
           41052684708299085211399427365734116182760315001271, 65378607361501080857009149939512557028198746004375,
           35829035317434717326932123578154982629742552737307, 94953759765105305946966067683156574377167401875275,
           88902802571733229619176668713819931811048770190271, 25267680276078003013678680992525463401061632866526,
           36270218540497705585629946580636237993140746255962, 24074486908231174977792365466257246923322810917141,
           91430288197103288597806669760892938638285025333403, 34413065578016127815921815005561868836468420090470,
           23053081172816430487623791969842487255036638784583, 11487696932154902810424020138335124462181441773470,
           63783299490636259666498587618221225225512486764533, 67720186971698544312419572409913959008952310058822,
           95548255300263520781532296796249481641953868218774, 76085327132285723110424803456124867697064507995236,
           37774242535411291684276865538926205024910326572967, 23701913275725675285653248258265463092207058596522,
           29798860272258331913126375147341994889534765745501, 18495701454879288984856827726077713721403798879715,
           38298203783031473527721580348144513491373226651381, 34829543829199918180278916522431027392251122869539,
           40957953066405232632538044100059654939159879593635, 29746152185502371307642255121183693803580388584903,
           41698116222072977186158236678424689157993532961922, 62467957194401269043877107275048102390895523597457,
           23189706772547915061505504953922979530901129967519, 86188088225875314529584099251203829009407770775672,
           11306739708304724483816533873502340845647058077308, 82959174767140363198008187129011875491310547126581,
           97623331044818386269515456334926366572897563400500, 42846280183517070527831839425882145521227251250327,
           55121603546981200581762165212827652751691296897789, 32238195734329339946437501907836945765883352399886,
           75506164965184775180738168837861091527357929701337, 62177842752192623401942399639168044983993173312731,
           32924185707147349566916674687634660915035914677504, 99518671430235219628894890102423325116913619626622,
           73267460800591547471830798392868535206946944540724, 76841822524674417161514036427982273348055556214818,
           97142617910342598647204516893989422179826088076852, 87783646182799346313767754307809363333018982642090,
           10848802521674670883215120185883543223812876952786, 71329612474782464538636993009049310363619763878039,
           62184073572399794223406235393808339651327408011116, 66627891981488087797941876876144230030984490851411,
           60661826293682836764744779239180335110989069790714, 85786944089552990653640447425576083659976645795096,
           66024396409905389607120198219976047599490197230297, 64913982680032973156037120041377903785566085089252,
           16730939319872750275468906903707539413042652315011, 94809377245048795150954100921645863754710598436791,
           78639167021187492431995700641917969777599028300699, 15368713711936614952811305876380278410754449733078,
           40789923115535562561142322423255033685442488917353, 44889911501440648020369068063960672322193204149535,
           41503128880339536053299340368006977710650566631954, 81234880673210146739058568557934581403627822703280,
           82616570773948327592232845941706525094512325230608, 22918802058777319719839450180888072429661980811197,
           77158542502016545090413245809786882778948721859617, 72107838435069186155435662884062257473692284509516,
           20849603980134001723930671666823555245252804609722, 53503534226472524250874054075591789781264330331690]
    print str(sum(arr))[0:10]


def euler14():
    maxChain = 0
    start = -1
    for i in range(1,1000001):
        ch = findChainLength(i)
        if ch > maxChain:
            start = i
            maxChain = ch
    print start, maxChain


def euler15():
    # Since the terms of the question allow at each step to go either (R) right or (D) down
    # it can be reduced to a simple combinatorial question on how many strings of 2*n length with equal number of
    # Rs and Ds we can create
    n = 20
    calc = math.factorial(2*n) // math.factorial(n) // math.factorial(n)
    print calc
    print "Number of routes are there through a 20*20 grid is: " + str(calc)


def euler16():
    p = math.pow(2,1000)
    digits = [int(d) for d in str(int(p))]
    print sum(digits)


def euler17():

    numletters = 0
    for i in range(1001):
       numletters += numberOfLetters(i)
    print numletters

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


def main():
    euler2()
    euler3()
    euler4()
    euler5()
    euler6()
    euler7()
    euler8()
    euler9()
    euler10()
    euler11()
    euler12()
    euler13()
    euler14()
    euler15()
    euler16()
    euler17()

if __name__ == "__main__":
    main()