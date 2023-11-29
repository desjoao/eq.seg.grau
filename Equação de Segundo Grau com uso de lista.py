def RaizQuadrada(a, b, delta):
    sqrt1 = ((-b) + delta**0.5)/(2*a)
    sqrt2 = ((-b) - delta**0.5)/(2*a)
    return sqrt1, sqrt2

def Delta(a, b, c):
    delta = b**2-4*a*c
    if delta >= 0:
        return delta
    else:
        return None

A = int(input('Informe o coeficiente angular da equação de 2º grau: '))
while A == 0:
    print('O coeficiente não pode ser nulo')
    A = int(input('Informe o coeficiente angular da equação de 2º grau: '))
B = int(input('Informe o coeficiente linear da equação de 2º grau: '))
C = int(input('Informe o coeficiente contante da equação de 2º grau: '))

delta = Delta(A, B, C)
raiz = []
if delta == None:
    print('Não há raíz definida nos conjuntos dos números reais.')
else:
    raiz.append(RaizQuadrada(A, B, delta))

print(f'As raízes da equação [{A}x² + {B}x + {C} = 0] são: {raiz}')
