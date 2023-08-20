"""

DECORATORS

Implementati urmatorii decoratori:
timeit – decorator care masoara timpul de executie al unei functii
logger – decorator care printeaza argumentele de intrare, si rezultatul unei functii
"""
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"timpul trecut este:{elapsed_time}")
        return res

    return wrapper

@timeit
def describe_vremea(grade):
    time.sleep(5)
    return(f'Vremea e frumoasa afara.Grade {grade}')


@timeit
def descrie_stare_spirit():

    time.sleep(3)
    return('Visatoare')


print(describe_vremea(23))
print(descrie_stare_spirit())


d = {'alpha':1, 'beta':2, 'gama':3}
dk = (d.keys())
print(dk)
print(type(dk))