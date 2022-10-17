import json

with open('unseJP_DB.json', 'r', encoding='utf-8') as unseDB:
    unseData = json.load(unseDB)


def leadingIndex(usrInput):
    returnUnse = list()
    returnUnse.append(unseData[usrInput - 1]['GoodOrBad'])
    returnUnse.append(unseData[usrInput - 1]['TotalUnse'])
    return returnUnse





