'''
David e Golias - O Lançamento com uma Funda

Por Lucas Costanzo e Pedro Cunial
'''
from numpy import linspace, pi
from math import sin, cos, degrees, asin, acos 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

massa = 0.33	#massa da pedra, será desconsiderada na rotação
hDavid = 1.57	#alturas
hGolias = 2.9
funda = .1
L = funda/2	#o tamanho da funda esticada é de 0.9m, mas por ser dobrada ao meio divide-se por dois
dAltura = hGolias - L	 #diferença de altura
hLancamento = 1 #medimos a Gabi rodando uma funda, é a distância do pé dela até o ponto mais baixo da rotação
g = 10
angulo = degrees(45)	#angulo de lançamento
diametro = 0.06	#diametro da pedra
# constanteAr = 0.25		#constante relativa a formula da resistencia do ar
# resAr = diametro * constanteAr	#calculo da resistencia do ar
aAngular = 1
mao = 0.1

T = linspace(0,5,1001)

def func1(V,T):
	theta = (aAngular*T*T)/2 	#definição do angulo atual (em radianos) em função da aceleração angular e tempo 
	xm = mao * cos(theta)		#posição da mão no eixo x
	ym = mao * sin(theta)		#posição da mão no eixo y
	vxm = -mao * aAngular * T * sin(theta)	#velocidade da mão no eixo x
	vym = mao * aAngular * T * cos(theta)	#velocidade da mão no eixo y

	sina = (V[1]-ym)/L
	cosa = (V[0]-xm)/L
	# sinb = 1 - (sina**2)**(1/2)
	# cosb = 1 - (cosa**2)**(1/2)


	vmf = vxm * cosa + vym * sina
	vpf = vmf
	vpp = 0

	dxpdt = vpf * cosa
	dypdt = vpf * sina
	
	return [dxpdt,dypdt]

M0 = [mao,-L]

M = odeint(func1,M0,T)




# plt.figure(figsize = (7,7))

plt.title('Espaço')
# plt.axis([-mao,mao,-mao,mao])
plt.plot(M[:,0],M[:,1],'g')
plt.show()

