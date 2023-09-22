name = input()

for i in range(len(name)):
    if name[i].isupper():
        print(name[i], end='')
