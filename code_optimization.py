file = open("codeopt.txt","r+")
filecontent = file.read()
split = filecontent.split()
print(split)

lhs = []
rhs = []

for i in split:
    temp = i.split("=")
    lhs.append(temp[0])
    rhs.append(temp[1])

#dead code elimination
for i in range(len(lhs)-2):
    temp = 0
    for j in rhs:
        if lhs[i] in j:
            temp+=1
    if temp == 0:
        lhs.pop(i)
        rhs.pop(i)
print()
print("After Dead code Elimination")
for i in range(len(lhs)):
     print(lhs[i]+"="+rhs[i])
print()



#Eliminate common expression
for i in range(len(lhs)):
    for j in range(len(rhs)):
        if i!=j and rhs[i]==rhs[j]:
            temp = lhs[i]
            for k in range(len(rhs)):
                if lhs[j] in rhs[k]:
                    rhs[k] = rhs[k].replace(lhs[j],lhs[i])
            lhs[j] = lhs[i]
print()
print("Eliminate common expression")
for i in range(len(lhs)):
     print(lhs[i]+"="+rhs[i])
print()


#code optimization
l=0
m=0
while l < len(lhs):
    while m < len(lhs):
        if l!=m and lhs[l]==lhs[m]:
            lhs.pop(m)
            rhs.pop(m)
        m+=1
    l+=1

        

code = []
for i in range(len(lhs)):
    code.append(lhs[i]+"="+rhs[i])

print("After Optimization")
for i in code:
    print(i)