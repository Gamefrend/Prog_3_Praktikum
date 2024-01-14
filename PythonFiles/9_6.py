
def permutationen(lst):
    n = len(lst)
    if n == 0:
        yield []
    elif n == 1:
        yield lst
    else:
        for i in range(n):
            rest = lst[:i] + lst[i+1:]
            for y in permutationen(rest):
                yield [lst[i]] + y


for e in permutationen([1, 2, 3]):
    print(e)
