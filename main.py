entrada = input()
a = entrada.replace('', '.')
c = a.replace('.', '', 1)
cpf = c.split('.')
resultado1 = []
resultado2 = []
soma1 = 0
soma2 = 0
y1 = 10
y2 = 11


for f in range(0, 9):
    resultado1.append(int(cpf[f]) * y1)
    y1 -= 1

    soma1 += int(resultado1[f])

for f in range(9):
    resultado2.append(int(cpf[f]) * y2)
    y2 -= 1

    soma2 += int(resultado2[f])


t = soma1 % 11
r = 11 - t

if r >= 10:
    r = 0

soma2 += r * 2

t2 = soma2 % 11
r2 = 11 - t2

if r2 >= 10:
    r2 = 0

if r == int(cpf[9]) and r2 == int(cpf[10]):
    print("Verdadeiro")
else:
    print("Falso")
