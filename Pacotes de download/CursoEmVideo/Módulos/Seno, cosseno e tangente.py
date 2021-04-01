from math import cos, sin, tan, radians
a = int(input('Digite um ângulo: '))
c = cos(radians(a))
s = sin(radians(a))
t = tan(radians(a))
print('O ângulo {} possui cosseno {:.2f}, seno {:.2f} e tangente {:.2f}'.format(a,c,s,t))