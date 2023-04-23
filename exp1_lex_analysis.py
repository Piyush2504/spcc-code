import keyword
import re

keywords = keyword.kwlist
operators = ['+', '-', '*', '/', '=', '==', '%']
seperators = ['"',"'", ',', ';', ":", '(', ')', '[', ']', '{', '}', '#', '|']
identifier = re.compile(r'[a-zA-Z_][\w_]*')
tokenizer = re.compile(r'\b\w+\b|\+|\-|\*|\/|\=|\=\=|\%|\"|\'|\,\;|\:|\(|\)|\[|\]|\{|\}|\#|\|')


with open('lex_input.txt') as f:
    for l in f.readlines():
        tokens = tokenizer.findall(l)
        for token in tokens:
            if token in keywords:
                print(f"{token}\t=>\tKeyword")
            elif token in operators:
                print(f"{token}\t=>\tOperator")
            elif token in seperators:
                print(f"{token}\t=>\tSeperator")
            elif identifier.fullmatch(token):
                print(f"{token}\t=>\tIdentifier")
            else:
                print(f"{token}\t=>\tLiteral")