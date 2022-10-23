import json
import random

with open('unseJP_DB.json', 'r', encoding='utf-8') as unseDB:
    unseData = json.load(unseDB)


def leadingIndex():
    returnUnse = list()
    randNum = random.randrange(1, 61)
    returnUnse.append(unseData[randNum - 1]['GoodOrBad'])
    returnUnse.append(unseData[randNum - 1]['TotalUnse'])
    return returnUnse








