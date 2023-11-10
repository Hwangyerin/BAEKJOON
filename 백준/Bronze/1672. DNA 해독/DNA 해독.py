DNA = {'AA':'A','AG':'C','AC':'A','AT':'G','GA':'C','GG':'G','GC':'T','GT':'A',
       'CA':'A','CG':'T','CC':'C','CT':'G','TA':'G','TG':'A','TC':'G','TT':'T'}

n=int(input())
dna = list(input())
while True:
    if len(dna)==1:
        break
    last_dna = dna[-2]+dna[-1]
    if last_dna in DNA:
        del dna[-2:]
        dna.append(DNA.get(last_dna))
print(*dna)
