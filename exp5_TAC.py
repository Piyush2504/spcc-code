from pprint import pprint

infix = input("Enter Expression: ")

operators = {'+': 1, '-': 1, '/': 2, '*': 2, '^': 3, '(': 0, '=': 0}

def infixToPostfix(infix):
    stack = []
    postfix = ""

    for ii, i in enumerate(infix):
        # print(i, stack, postfix)
        if i == " ":
            continue
        if i.isalnum():
            postfix += i
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            if infix[ii-1] in operators:
                postfix += 'u'
            else:
                while stack and operators[i] <= operators[stack[-1]]:
                    postfix += stack.pop()
                stack.append(i)
    while stack:
        postfix += stack.pop()
    return postfix


exp = infixToPostfix(infix)
print("Postfix:", exp)

tac = {}
stack = []
i = j = 0
while i < len(exp):
    # print(exp[i], tac, stack)
    if exp[i] == 'u':
        tac['t'+str(j)] = '-'+exp[i+1]
        stack.append('t'+str(j))
        i += 2
        j += 1
    elif exp[i] in operators:
        op2 = stack.pop()
        op1 = stack.pop()
        tac['t'+str(j)] = f"{op1} {exp[i]} {op2}"
        stack.append('t'+str(j))
        i += 1
        j += 1
    else:
        stack.append(exp[i])
        i += 1
for k, v in tac.items():
    if '=' in v:
        print(v)
    else:
        print(f"{k} = {v}")




