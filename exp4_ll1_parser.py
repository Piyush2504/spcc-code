import re
from collections import defaultdict

import pandas as pd

grammar = {}
first = defaultdict(set)
follow = defaultdict(set)
parseTable = defaultdict(set)
start = ""

# Reading Input File
with open("first_follow_input.txt") as f:
    for l in f.readlines():
        tokens = re.split(" |->|\n|\|", l)
        leftProd = tokens.pop(0)
        rightProd = []
        for t in tokens[1:]:
            if t != '':
                rightProd.append(t)
        grammar[leftProd] = rightProd
        if not start:
            start = leftProd
print(f"Grammar:")
for k, v in grammar.items():
    print(f"{k} => {v}")


def cal_first(s):
    if not s.isupper():
        return {s}
    if first[s]:
        return first[s]
    for i in grammar[s]:
        j = 0
        if i[j].isupper():
            f = cal_first(i[j]).copy()
            j += 1
            while j < len(i) and '@' in f:
                f.remove('@')
                first[s].update(f)
                f = cal_first(i[j]).copy()
                j += 1
            first[s].update(f)
        else:
            first[s].add(i[j])
    return first[s]


def cal_follow(s):
    if follow[s]:
        return follow[s]
    if s == start:
        follow[s].add('$')
    for i in grammar:
        for j in grammar[i]:
            for k in range(len(j)):
                if j[k] == s:
                    l = k + 1
                    if l < len(j):
                        f = cal_first(j[l]).copy()
                        while True:
                            if '@' in f:
                                f.remove('@')
                                follow[s].update(f)
                                l += 1
                                if l < len(j):
                                    f = cal_first(j[l]).copy()
                                else:
                                    if i == s:
                                        break
                                    f = cal_follow(i).copy()
                            else:
                                follow[s].update(f)
                                break
                    else:
                        if i == s:
                            break
                        f = cal_follow(i).copy()
                        follow[s].update(f)
    return follow[s]


def parser():
    for i in grammar:
        for j in grammar[i]:
            if j == '@':
                for k in follow[i]:
                    parseTable[i, k].add(j)
            else:
                if j[0].isupper():
                    for k in first[j[0]]:
                        parseTable[i, k].add(j)
                else:
                    parseTable[i, j[0]].add(j)


for p in grammar:
    cal_first(p)
print("\nFirst:")
for k, v in first.items():
    print(f"{k} => {v}")

for p in grammar:
    cal_follow(p)
print("\nFollow:")
for k, v in follow.items():
    print(f"{k} => {v}")

parser()
print("\nParse Table:")
# for k, v in parseTable.items():
#     print(f"{k} => {v}")
new_table = defaultdict(dict)
for i, j in parseTable.items():
    new_table[i[1]][i[0]] = ",".join(j)
print(pd.DataFrame(new_table).fillna('-'))
