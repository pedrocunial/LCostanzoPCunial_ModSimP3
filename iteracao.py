'''
David e Golias - O Lançamento com uma Funda

Por Lucas Costanzo e Pedro Cunial
'''
from numpy import linspace, pi
from math import sin, cos, degrees 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

massa = 0.33	#massa da pedra
hDavid = 1.57	#alturas
hGolias = 2.9
funda = 0.9/2	#o tamanho da funda esticada é de 0.9m, mas por ser dobrada ao meio divide-se por dois
dAltura = hGolias - funda	 #diferença de altura
hLancamento = 1 #medimos a Gabi rodando uma funda
g = 10
angulo = degrees(45)	#angulo de lançamento
diametro = 0.06	#diametro da pedra
# constanteAr = 0.25		#constante relativa a formula da resistencia do ar
# resAr = diametro * constanteAr	#calculo da resistencia do ar
aAngular = 1
mao = 0.1

T = linspace(0,4,100)

def func1(Y,T):
	frequencia = aAngular * T
	dxdt = sin(frequencia**2)
	print(dxdt)
	dydt = cos(frequencia**2)
	print(dydt)
	dvxdt = 2 * T * Y[1]
	dvydt = -2 * T * Y[0]
	# dwdt = 2 * pi * frequencia
	# dvdt = dwdt * mao
	return [dxdt,dydt,dvxdt,dvydt]
	# return [dwdt,dvdt]

M0 = [0,-mao,0,0]
M = odeint(func1,M0,T)
S = [0]*len(T)

for m in range(len(T)):
	resul = (M[0][m]**2 + M[1][m]**2)**(1/2)
	S[m] = resul

# M0 = [0,0]
# M = odeint(func1,M0,T)

plt.title('Eu gosto de feijão kkkkkkkj\'')
plt.plot(S,T,'g')
plt.show()