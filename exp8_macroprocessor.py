MDT = []
MNT = []
ALA = []
MDTC = MNTC = 0

with open("macroprocessor.txt") as f:
    code = []
    for l in f.readlines():
        l = l.strip()
        code.append(l)

i = 0
while i < len(code):
    if code[i] == 'MACRO':
        i += 1
        macro = []
        while code[i] != 'MEND':
            macro.append(code[i])
            i += 1
        macro.append('MEND')

        for j in macro[0].split():
            if j[0] != '&':
                MNT.append((j, MDTC))
            else:
                ALA.append(j)

        for j in macro:
            l = ""
            for k in j.split():
                if k in ALA:
                    l += '#' + str(ALA.index(k)) + " "
                else:
                    l += k + " "
            MDT.append(l)

        MDTC = i
    i += 1
print("\nMacro Definition Table:")
print("Index\t\tDefinition")
for ii, i in enumerate(MDT):
    print(f"{ii}\t\t{i}")
# print(MDT)
print("\nMacro Name Table:")
print("Index\t\tName\t\t\tMDT Index")
for ii, i in enumerate(MNT):
    print(f"{ii}\t\t{i[0]:b<8}\t\t\t{i[1]}")
# print(MNT)
print("\nArgument List Array:")
print("Index\t\tArgument")
for ii, i in enumerate(ALA):
    print(f"{ii}\t\t{i[1:]:b<8}")
# print(ALA)


