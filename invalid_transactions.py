"""
Invalid Transaction:https://leetcode.com/problems/invalid-transactions/
"""

from collections import defaultdict

#First way
def invalidTrans(transactions):
    invalid = {}
    result = []

    for trans in transactions:
        name, time, amount, city = trans.split(',')
        time, amount = int(time), int(amount)

        if time not in invalid:
            invalid[time] = {name : [city]}
        else:
            if name not in invalid[time]:
                invalid[time][name] = [city]
            else:
                invalid[time][name].append[city]
   
    for trans in transactions:
        name, time, amount, city = trans.split(',')
        time, amount = int(time), int(amount)

        if amount > 1000:
            result.append(trans)

        for t in range(time - 60, time + 61):
            if t not in invalid:
                continue
            if name not in invalid[t]:
                continue
            if len(invalid[t][name]) > 1 or (invalid[t][name][0] != name):
                result.append(trans)
                break

    return result

# Method with sorting
def invalidTransaction(transactions):
    invalid = defaultdict(list)
    result = set()
    transactions = [t.split(',') for t in transactions]
    transactions.sort(key=lambda x: int(x[1]))

    for i, trans in enumerate(transactions):
        name, time, amount, city = trans
        time, amount = int(time), int(amount)
        if amount > 1000:
            result.add(i)
        if name in invalid:
            id = len(invalid[name]) - 1
            while id>=0 and time - int(transactions[invalid[name][id]][1]) <= 60:
                if transactions[invalid[name][id]][3] != city:
                    result.add(i)
                    result.add(invalid[name][id])
                id -= 1
        invalid[name].append(i)

    return [','.join(transactions[i]) for i in result]


print(invalidTransaction(["alice,20,800,mtv","bob,50,1200,mtv"]))