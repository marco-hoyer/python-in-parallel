from math import sqrt

from joblib import delayed, Parallel


def producer():
    for i in range(6):
        print('Produced %s' % i)
        yield i


out = Parallel(n_jobs=2, verbose=100, pre_dispatch='1.5*n_jobs')(delayed(sqrt)(i) for i in producer())
