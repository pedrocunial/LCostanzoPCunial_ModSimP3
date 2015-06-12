'''
David e Golias - O Lançamento com uma Funda

Por Lucas Costanzo e Pedro Cunial
'''
from numpy import linspace
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
constanteAr = 0.25		#constante relativa a formula da resistencia do ar
resAr = diametro * constanteAr	#calculo da resistencia do ar

T = linspace(0,100,1000)

def func1(Y,T):
	
