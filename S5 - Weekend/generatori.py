"""

Generators

Implementati un generator pentru loteria 6/49 si noroc:
Primele 6 apelari catre generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur numar de “noroc” format din 7 cifre

"""
import random
def gen_loto_numbers():
    for nr in range(1, 7):
        yield random.randint(1, 50)
    yield random.randint(1_000_000, 9_999_999)

# def loto_gen():
#     my_list = random.sample(range(1,50),6)
#     for nr in my_list:
#         yield nr
#     yield random.randint(1_000_000, 9_999_999)

print(gen_loto_numbers())

for numar_loto in gen_loto_numbers():
    print(numar_loto)