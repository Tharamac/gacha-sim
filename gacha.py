import decimal
import random
from decimal import *
import math
import json

with open('gacha_config.json', "r") as file:
    json_str = file.read()
gacha_config = json.loads(json_str)

rarity_probabity_precent = {
    key: value["probability"].split(sep="%")[0] for key, value in gacha_config.items()
}

e = max([abs(Decimal(rate).as_tuple().exponent) for rate in rarity_probabity_precent.values()])
max_range = 100 * 10**e

rarity_probabity_int = {}    
start = 1
for rarity, rate in rarity_probabity_precent.items():
    rate_int = round(int(rate) * 10**e)
    rarity_probabity_int[rarity] = range(start, start + rate_int)
    start += rate_int


while True:
    number_of_rolls = int(input("Number of rolls (1,10):"))
    if number_of_rolls == 1 or number_of_rolls == 10:
        break
    else:
        print("invalid number of rolls")

# rate_str = "10%"
# rate_percent = rate_str.split(sep="%")[0]
# e = abs(Decimal(rate_percent).as_tuple().exponent)
# rate_int = round(float(rate_percent) * 10**e)
# print(rate_int)
# max_range = 100 * 10**e
randomlist = random.sample(range(1, max_range + 1), number_of_rolls)
record = []
for num in randomlist:
    for rarity, condition_range in rarity_probabity_int.items():
        if num in condition_range:
            item_gotten = random.choice(gacha_config[rarity]["items"])
            entry = ">>> (%s)\t%s" % ("☆" * gacha_config[rarity]["rarity"], item_gotten)
            record.append(entry)
            print(entry)
            break
    print("-" * 10)
    input("Continue?")
    print("-" * 10)
print("-" * 10)
print("Rolls Summary:")
print("-" * 10)
for entry in record:
    print(entry)
print("-" * 10)