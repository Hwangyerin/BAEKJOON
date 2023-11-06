eng = input().strip()
eng = eng.lower()
while eng != '#':
    print(eng[0],eng[1:].count(eng[0]))
    eng = input().strip()
    eng = eng.lower()
