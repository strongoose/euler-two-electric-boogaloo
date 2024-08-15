from typing import Iterator, Iterable

import itertools
from math import sqrt, floor


def until(limit: int, it: Iterable[int]) -> Iterable[int]:
    return itertools.takewhile(
        lambda x: x < limit,
        it,
    )


def p1() -> int:
    return sum([n for n in range(1, 1000) if n % 3 == 0 or n % 5 == 0])


def fibonacci() -> Iterator[int]:
    prev: int = 1
    yield prev
    curr: int = 1
    yield curr
    while True:
        curr, prev = curr + prev, curr
        yield curr


def p2() -> int:
    return sum([n for n in until(4_000_000, fibonacci()) if n % 2 == 0])


def primes() -> Iterator[int]:
    primes = [2]
    yield 2

    def isprime(n: int) -> bool:
        # return all(map(lambda p: n % p != 0, primes))
        for p in primes:
            if n % p == 0:
                return False
        return True

    i = 3
    while True:
        if isprime(i):
            primes.append(i)
            yield i
        i += 2


def prime_factors(n: int) -> list[int]:
    dividend = n
    factors = []

    for p in itertools.takewhile(lambda x: x <= sqrt(dividend), primes()):
        while dividend % p == 0:
            dividend = dividend // p
            factors.append(p)

    # The remaining dividend is the last prime factor
    # This can be 1 sometimes - for example, finding the prime factors of 4
    if dividend != 1:
        factors.append(dividend)
    return factors


def p3() -> int:
    return prime_factors(600851475143)[-1]


def is_palindrome(n: int) -> bool:
    word = str(n)

    while word != "":
        if word[0] != word[-1]:
            return False

        word = word[1:-1]

    return True


def p4() -> int:
    max = 0

    for a in range(1, 1000):
        for b in range(1, 1000):
            product = a * b
            if product > max and is_palindrome(product):
                max = a * b

    return max


def product(ns: Iterable[int]) -> int:
    res = 1
    for n in ns:
        res = res * n
    return res


def p5() -> int:
    """
    My intuition was wrong with this one - initially I thought we could just take all the primes under 20 and multiply them... but if we do that the result won't divide by, e.g., 4 (== 2 * 2)
    """
    factors = []

    for p in until(20, primes()):
        # We add this prime factor n times, where n is the largest integer for which factor**n < 20
        # i.e., the floor of the nth root of 20
        repeats = floor(20 ** (1 / p))

        for _ in range(0, repeats):
            factors.append(p)

    return product(factors)


def p6() -> int:
    sum_of_squares = sum(n**2 for n in range(0, 101))
    square_of_sum = sum(range(0, 101)) ** 2

    return square_of_sum - sum_of_squares


def p7() -> int:
    # This takes a second or so, so commenting out to speed up feedback
    return [*itertools.islice(primes(), 10_000)][-1]


def windows(input: Iterable[int], width: int) -> Iterator[list[int]]:
    iterator = iter(input)
    window: list[int] = []

    for i in range(0, width):
        window.append(next(iterator))
    yield window[:]

    for n in iterator:
        window.pop(0)
        window.append(n)
        yield window[:]


def p8() -> int:
    input = "".join(
        """
      73167176531330624919225119674426574742355349194934
      96983520312774506326239578318016984801869478851843
      85861560789112949495459501737958331952853208805511
      12540698747158523863050715693290963295227443043557
      66896648950445244523161731856403098711121722383113
      62229893423380308135336276614282806444486645238749
      30358907296290491560440772390713810515859307960866
      70172427121883998797908792274921901699720888093776
      65727333001053367881220235421809751254540594752243
      52584907711670556013604839586446706324415722155397
      53697817977846174064955149290862569321978468622482
      83972241375657056057490261407972968652414535100474
      82166370484403199890008895243450658541227588666881
      16427171479924442928230863465674813919123162824586
      17866458359124566529476545682848912883142607690042
      24219022671055626321111109370544217506941658960408
      07198403850962455444362981230987879927244284909188
      84580156166097919133875499200524063689912560717606
      05886116467109405077541002256983155200055935729725
      71636269561882670428252483600823257530420752963450
    """.split()
    )

    digits = [int(c) for c in input]

    max = 0
    for window in windows(digits, 13):
        if (x := product(window)) > max:
            max = x

    return max


def isqrt(n: int) -> int | None:
    def iterate(guess: float) -> float:
        return (guess + n / guess) / 2

    prev = n / 2
    guess = iterate(prev)

    while abs(guess - prev) >= 0.5:
        prev, guess = guess, iterate(guess)

    root = floor(guess)

    if root * root == n:
        return root
    else:
        return None


def pythagorean_triplets() -> Iterator[tuple[int, int, int]]:
    for a in range(1, 1000):
        for b in range(a, 1000):
            if c := isqrt(a**2 + b**2):
                yield (a, b, c)


def p9() -> int:
    for a, b, c in pythagorean_triplets():
        if a + b + c == 1000:
            return a * b * c

    # Unreachable
    assert False


def sieve(n: int) -> list[int]:
    """
    There are two key optimisations in here that have made this problem tractable in less than a second or so
     - Instead of iterating through the sieve marking numbers as non-prime, use slice assignment. This is a _lot_ faster.
     - A much smaller optimisation which still helps a bit is only running over non-even numbers in the sieve range.
    """
    sieve = [True] * (n + 1)

    def sieve_for(n: int) -> None:
        start = n * 2
        products = len(sieve[start::n])
        sieve[start::n] = [False] * products

    limit = int(n**0.5) + 1
    sieve_for(2)
    for i in range(3, limit, 2):
        sieve_for(i)

    return [n for n, isprime in enumerate(sieve) if isprime and n > 1]


def p10() -> int:
    return sum(sieve(2_000_000))


def diagonals(arr: list[list[int]]) -> Iterator[list[int]]:
    """
       0 1                 1
       2 3 -> diagonals -> 0 3
       4 5                 2 5
                           4

                             2
       0 1 2                 1 5
       3 4 5 -> diagonals -> 0 4 8
       6 7 8                 3 7
                             6

    Number of diagonals = h + w - 1

    We read out the diagonals from top right to bottom left, as in the examples above.

    The function assumes that the array is a regular grid i.e. no uneven line lengths.
    """
    height = len(arr)
    width = len(arr[0])

    start_indices: list[tuple[int, int]] = [
        # Top row (y = 0) (in reverse order)
        *[(x, 0) for x in range(width - 1, -1, -1)],
        # Left column (x = 0) (excluding (0, 0), which is included in the top row)
        *[(0, y) for y in range(1, height)],
    ]

    diag = []
    for x, y in start_indices:
        while x < width and y < height:
            diag.append(arr[y][x])
            x, y = x + 1, y + 1
        yield diag
        diag = []


def transpose(arr: list[list[int]]) -> list[list[int]]:
    width = len(arr[0])
    return [[row[x] for row in arr] for x in range(0, width)]


def flip_y(arr: list[list[int]]) -> list[list[int]]:
    return arr[::-1]


def p11() -> int:
    input = [
        [*map(int, line.split())]
        for line in """
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    """.strip().split("\n")
    ]

    res = 0

    # Horizontal
    for line in input:
        for w in windows(line, 4):
            res = max(product(w), res)

    # Diagonal (down-right)
    for diag in diagonals(input):
        if len(diag) >= 4:
            for w in windows(diag, 4):
                res = max(product(w), res)

    # Transpose for verticals
    input = transpose(input)
    for line in input:
        for w in windows(line, 4):
            res = max(product(w), res)

    # Flip for up-left diags
    input = flip_y(input)
    for diag in diagonals(input):
        if len(diag) >= 4:
            for w in windows(diag, 4):
                res = max(product(w), res)

    return res


def triangle_numbers() -> Iterator[int]:
    tri = 0
    for i in itertools.count(start=1):
        tri += i
        yield tri


def p12() -> int:
    for n in triangle_numbers():
        pfs = prime_factors(n)

        # An upper bound on the number of factors for a number with p prime factors is
        #  sum([p choose i] for i in range(1, p + 1))
        # This works out to be 2**p - 1 for reasons I don't entirely comprehend.
        #
        # Anyway this makes this problem run marginally faster

        upper_bound = 2 ** len(pfs) - 1
        if upper_bound < 500:
            continue

        # According to some random Maths StackExchange, if n = p1**v1 * p2**v2 * ... * pk**vk
        # then the number of factors of n is
        #   product([vi + 1] for vi in [v1, ..., vk])
        pfs_counts: dict[int, int] = {}
        for pf in pfs:
            if pf not in pfs_counts.keys():
                pfs_counts[pf] = 1
            else:
                pfs_counts[pf] += 1

        nfactors = product([v + 1 for v in pfs_counts.values()])

        if nfactors > 500:
            return n

    # Unreachable
    assert False


def bigsum(*ns: list[int]) -> list[int]:
    """
    Sum some big numbers. Each number should be provided as a list of single digits.
    """

    # Theoretically we should pad the ns with leading 0s to make them equal width. We have known input, so I'm not
    # going to bother.
    width = len(ns[0])

    digits = []
    carry = 0
    for i in range(width - 1, -1, -1):
        col_sum = sum(int(n[i]) for n in ns) + carry

        digits.append(str(col_sum % 10))
        carry = col_sum // 10

    digits = digits[::-1]
    digits = [*str(carry)] + digits

    return [*map(int, digits)]


def p13() -> int:
    input = [
        [int(digit) for digit in row]
        for row in """
    37107287533902102798797998220837590246510135740250
    46376937677490009712648124896970078050417018260538
    74324986199524741059474233309513058123726617309629
    91942213363574161572522430563301811072406154908250
    23067588207539346171171980310421047513778063246676
    89261670696623633820136378418383684178734361726757
    28112879812849979408065481931592621691275889832738
    44274228917432520321923589422876796487670272189318
    47451445736001306439091167216856844588711603153276
    70386486105843025439939619828917593665686757934951
    62176457141856560629502157223196586755079324193331
    64906352462741904929101432445813822663347944758178
    92575867718337217661963751590579239728245598838407
    58203565325359399008402633568948830189458628227828
    80181199384826282014278194139940567587151170094390
    35398664372827112653829987240784473053190104293586
    86515506006295864861532075273371959191420517255829
    71693888707715466499115593487603532921714970056938
    54370070576826684624621495650076471787294438377604
    53282654108756828443191190634694037855217779295145
    36123272525000296071075082563815656710885258350721
    45876576172410976447339110607218265236877223636045
    17423706905851860660448207621209813287860733969412
    81142660418086830619328460811191061556940512689692
    51934325451728388641918047049293215058642563049483
    62467221648435076201727918039944693004732956340691
    15732444386908125794514089057706229429197107928209
    55037687525678773091862540744969844508330393682126
    18336384825330154686196124348767681297534375946515
    80386287592878490201521685554828717201219257766954
    78182833757993103614740356856449095527097864797581
    16726320100436897842553539920931837441497806860984
    48403098129077791799088218795327364475675590848030
    87086987551392711854517078544161852424320693150332
    59959406895756536782107074926966537676326235447210
    69793950679652694742597709739166693763042633987085
    41052684708299085211399427365734116182760315001271
    65378607361501080857009149939512557028198746004375
    35829035317434717326932123578154982629742552737307
    94953759765105305946966067683156574377167401875275
    88902802571733229619176668713819931811048770190271
    25267680276078003013678680992525463401061632866526
    36270218540497705585629946580636237993140746255962
    24074486908231174977792365466257246923322810917141
    91430288197103288597806669760892938638285025333403
    34413065578016127815921815005561868836468420090470
    23053081172816430487623791969842487255036638784583
    11487696932154902810424020138335124462181441773470
    63783299490636259666498587618221225225512486764533
    67720186971698544312419572409913959008952310058822
    95548255300263520781532296796249481641953868218774
    76085327132285723110424803456124867697064507995236
    37774242535411291684276865538926205024910326572967
    23701913275725675285653248258265463092207058596522
    29798860272258331913126375147341994889534765745501
    18495701454879288984856827726077713721403798879715
    38298203783031473527721580348144513491373226651381
    34829543829199918180278916522431027392251122869539
    40957953066405232632538044100059654939159879593635
    29746152185502371307642255121183693803580388584903
    41698116222072977186158236678424689157993532961922
    62467957194401269043877107275048102390895523597457
    23189706772547915061505504953922979530901129967519
    86188088225875314529584099251203829009407770775672
    11306739708304724483816533873502340845647058077308
    82959174767140363198008187129011875491310547126581
    97623331044818386269515456334926366572897563400500
    42846280183517070527831839425882145521227251250327
    55121603546981200581762165212827652751691296897789
    32238195734329339946437501907836945765883352399886
    75506164965184775180738168837861091527357929701337
    62177842752192623401942399639168044983993173312731
    32924185707147349566916674687634660915035914677504
    99518671430235219628894890102423325116913619626622
    73267460800591547471830798392868535206946944540724
    76841822524674417161514036427982273348055556214818
    97142617910342598647204516893989422179826088076852
    87783646182799346313767754307809363333018982642090
    10848802521674670883215120185883543223812876952786
    71329612474782464538636993009049310363619763878039
    62184073572399794223406235393808339651327408011116
    66627891981488087797941876876144230030984490851411
    60661826293682836764744779239180335110989069790714
    85786944089552990653640447425576083659976645795096
    66024396409905389607120198219976047599490197230297
    64913982680032973156037120041377903785566085089252
    16730939319872750275468906903707539413042652315011
    94809377245048795150954100921645863754710598436791
    78639167021187492431995700641917969777599028300699
    15368713711936614952811305876380278410754449733078
    40789923115535562561142322423255033685442488917353
    44889911501440648020369068063960672322193204149535
    41503128880339536053299340368006977710650566631954
    81234880673210146739058568557934581403627822703280
    82616570773948327592232845941706525094512325230608
    22918802058777319719839450180888072429661980811197
    77158542502016545090413245809786882778948721859617
    72107838435069186155435662884062257473692284509516
    20849603980134001723930671666823555245252804609722
    53503534226472524250874054075591789781264330331690
    """.split()
    ]

    first_ten = [str(digit) for digit in bigsum(*input)[:10]]

    return int("".join(first_ten))


def collatz(n: int) -> Iterator[int]:
    while True:
        yield n
        match n:
            case 1:
                return
            case n if n % 2 == 0:
                n = n // 2
            case n:
                n = 3 * n + 1


def p14() -> int:
    # The naive way:
    result = 0
    longest = 0
    for i in range(1, 1_000_001):
        len_i = len([*collatz(i)])
        if len_i > longest:
            longest = len_i
            result = i

    return result
