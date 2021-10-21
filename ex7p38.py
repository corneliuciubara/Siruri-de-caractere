S = ['A','MATRICE','SIR','MA']
# a)
a=0
for i in S:
    for i in i:
        if i == "A":
            a = a+1
print('Numarul de aparitii ale caracterului A in sirul S:',a)

# b)
print('Sirul obinut prin substituirea caracterului A print caracterul * :',S.replace('A','*') )

# c)


# d)
d=0
for f in S:
    for f in f:
        if f == "MA":
            d = d+1
print('Numarul de aparitii ale silabei MA in sirul S:',d)

# e)
print(S.replace('MA','TA'))

# f)
print(S.replace('TO',''))

# g)
g=S
g.sort(reverse=True)
print('Scrierea inversa a sirului s:',g)
