f.open('c/Users/STATIE-6-C100/Desktop/Input.txt','w')
date = str(input('Sa se afiseze caracterele'))
f.write(date)
f.close()

f=open('c/Users/STATIE-6-C100/Desktop/Input.txt','r')
x = f.read()
print(x)
print(type(x))
z = []
for i in range(0, len(x)):
    if x[i] == 'o' or 'a':
        z[i] = x[i]

f.open('c/Users/STATIE-6-C100/Desktop/Exit.txt','w')
f.write('Caractere', 'n')
f.write('Numărul de vocale sunt: ')
