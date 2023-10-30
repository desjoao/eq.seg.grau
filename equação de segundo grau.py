import math
def delta (b, a, c):
    d = math.pow(b, 2) - 4*a*c
    if d >= 0:
        return d
    else:
        return None
def raiz (b, a, d):
    r1 = (-b + math.sqrt(d))/(2*a)
    r2 = (-b - math.sqrt(d))/(2*a)
    return r1, r2

a = int(input('Informe o valor do coeficiente angular da equação de segundo grau (a): '))
while a == 0:
    print('O coeficiente angular de uma equação de segundo grau não pode ser nulo.')
    a = int(input('Informe outro valor para o coeficiente angular da equação de segundo grau (a): '))

b = int(input('Informe o valor do coeficiente linear da equação de segundo grau (b): '))

c = int(input('Informe o valor do coeficiente constante da equação de segundo grau: '))

Delta = delta(b, a, c)
print(f'As raízes da equação de segundo grau {a}x²+{b}x+{c}=0 são: {raiz(b,a, Delta)}.')
