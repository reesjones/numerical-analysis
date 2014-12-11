import itertools
print(next(2** -k for k in itertools.count() if 1 + 2 ** -(1 + k) == 1))
