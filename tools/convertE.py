r'''
Convert 1.14E+09 in to 1.14 \times 10 ^ 9
'''
while True: # will RE, but let it be there
    a = input()
    b = ''
    for i in a:
        if (i == ' '):
            pass
        else:
            b += i
    a = b.split('&')
    for i in a:
        j = i.partition("E+")
        print(end='$')
        if j[0] == i:
            print(i, end='$&')
        elif (j[2][-1] != '\\'):
            print(j[0], "\\times 10^{", int(j[2]), "}", end='$&')
        else:
            print(j[0], "\\times 10^{", int(j[2][:-2]), "}", end='$\\\\')
    print('')
