L=list(input())
for i in range(len(L)):
    if L[i].isupper(): #대문자라면
        if ord(L[i])<78:
            L[i] = chr(ord(L[i])+13)
        else:
            L[i] = chr(ord(L[i])-13)
    elif L[i].islower():
        if ord(L[i])<110:
            L[i] = chr(ord(L[i])+13)
        else:
            L[i] = chr(ord(L[i])-13)
print(''.join(L))
