
import math

def equacao_1_grau(a, b):
    return -b / a

def equacao_2_grau(a,b,c):
    delta = b**2 - 4*a*c
    
    if delta < 0:
        yield "A equação não possui raízes reais."
    
    elif delta == 0:
        x = -b / (2*a)
        yield x
    
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        yield x1
        yield x2