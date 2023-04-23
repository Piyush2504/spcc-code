import re
from string import ascii_uppercase

grammar = {}

# Reading Input File
with open("left_recursion_input.txt") as f:
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
new_grammar = {}
for i in grammar:
    alpha = []
    beta = []
    found = False
    for j in grammar[i]:
        if j[0] == i:
            found = True
            alpha.append(j[1:])
        else:
            beta.append(j)
    if found:
        k = remaining.pop()
        new_grammar[i] = [c+k for c in beta]
        new_grammar[k] = [c+k for c in alpha] + ['@']
    else:
        new_grammar[i] = grammar[i]

if grammar == new_grammar:
    print("\nNo Left Recursion Found")
else:
    print(f"\nGrammar After removing Left Recursion:")
    for k, v in new_grammar.items():
        print(f"{k} => {v}")