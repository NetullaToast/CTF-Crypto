# 低加密指数广播攻击
import json
import math
import libnum
from gmpy2 import *


def read():
    with open("enc.txt", "r") as f:
        data = json.loads(f.read())
    return data


def broadcast():
    sum = 0
    for n_i, c_i in zip(n, c):
        N_i = N // n_i
        inv = gmpy2.invert(N_i, n_i)
        sum += c_i * N_i * inv
    return sum % N


data = read()
e = 10
c = [int(dat["c"]) for dat in data]
n = [int(dat["n"]) for dat in data]
N = math.prod(n)


m = broadcast()
while True:
    t = gmpy2.iroot(m, e)
    if t[1]:
        m = t[0]
        break
    else:
        m += N

flag = libnum.n2s(int(m)).decode()
print(flag)

"""
flag{wo0_th3_tr4in_i5_leav1ng_g3t_on_it}
"""
