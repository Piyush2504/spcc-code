import re
from collections import Counter, defaultdict
from string import ascii_uppercase

grammar = {}

# Reading Input File
with open("left_factoring_input.txt") as f:
    for l in f.readlines():
        tokens = re.split(" |->|\n|\|", l)
        leftProd = tokens.pop(0)
        rightProd = []
        for t in tokens[1:]:
            if t != '':
                rightProd.append(t)
        grammar[leftProd] = rightProd
print(f"Grammar:")
for k, v in grammar.items():
    print(f"{k} => {v}")

remaining = {*ascii_uppercase} - {i for i in grammar}

new_grammar = defaultdict(list)
while True:
    for i in grammar:
        c = Counter()
        alpha = defaultdict(list)
        for j in grammar[i]:
            c[j[0]] += 1
            alpha[j[0]].append(j[1:])
        for j in c.most_common():
            if j[1] > 1:
                k = remaining.pop()
                new_grammar[i].append(j[0]+k)
                new_grammar[k] = alpha[j[0]]
            else:
                new_grammar[i].append(j[0]+alpha[j[0]][0])

    if grammar == new_grammar:
        print("\nNo More Left Factoring Found")
        break
    else:
        print(f"\nGrammar After Left Factoring:")
        for k, v in new_grammar.items():
            print(f"{k} => {v}")
        grammar = new_grammar
        new_grammar = defaultdict(list)


