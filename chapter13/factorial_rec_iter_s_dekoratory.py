from functools import wraps

def timer(func):
    '''
    Dokumentační řetězec dekorátoru...
    '''
    import time

    @wraps(func)
    def wrapper(n):
        now = time.time()
        vysledek = func(n)
        end = time.time()
        print(f'Čas výpočtu: {end-now}s.')
        return vysledek
    return wrapper

@timer
def fac_rec(q):
    '''
    Výpočet faktoriálu pomocí rekurze...
    '''
    def fac(m):
        if m == 1:
            return 1
        else:
            return m * fac(m-1)
    return fac(q)

@timer
def fac_iter(n):
    '''
    Výpočet faktoriálu pomocí iterace...
    '''
    start = 1
    vysledek = 1
    for i in range(n):
        vysledek *= start
        start += 1

    return vysledek