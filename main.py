import math
pi=math.pi
print('Калькулятор для расчитывания площади цилиндра')
h=input('Введите высоту цилиндра \n')
d=input('Введите диаметр цилиндра \n')
R=float(d)/2
S=2*float(pi)*float(R)*float(h)+2*float(pi)*float(R**2)
print(S)
