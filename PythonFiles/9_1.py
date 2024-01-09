import math
def teiler(z):
    return [x for x in range(1, z) if z % x == 0 if x != 1]


def isPrime(x):
    if x % 2 == 0 and x != 2:
        return False
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

cubic = [int(math.pow(x, 3)) for x in range(11) if math.pow(x, 3) % 2 == 0]
prim = [x for x in range(10000, 11000) if isPrime(x)]

testZahl = 100
print(cubic)
print(teiler(testZahl))
print(prim)


def hochDrei(x):
    return int(math.pow(x, 3))


print(list(filter(lambda x: x % 2 == 0, map(hochDrei, range(11)))))
print(list(filter(lambda x: testZahl % x == 0 and x != 1, range(1, testZahl))))
print(list(filter(isPrime, range(10000, 11000))))
