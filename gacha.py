import decimal
import random
from decimal import *
import math

rate_str = "2%"
rate_percent = rate_str.split(sep="%")[0]
e = abs(Decimal(rate_percent).as_tuple().exponent)
rate_int = float(rate_percent) * 10**e
max_range = 100 * 10**e
randomlist = random.sample(range(1, max_range + 1), 10)
print(randomlist)
for num in randomlist:
    if(num <= rate_int):
        print("you got 5*")
    else:
        print("salt")
    input("continue?: ")