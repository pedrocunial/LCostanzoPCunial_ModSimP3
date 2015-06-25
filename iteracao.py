'''
David e Golias - O Lançamento com uma Funda

Por Lucas Costanzo e Pedro Cunial
'''

from numpy import linspace, pi
from math import sin, cos, degrees, asin, acos 
from scipy.integrate import odeint
import matplotlib.pyplot as plt

hDavid = 1.57	#alturas
hGolias = 2.9
funda = .75 	#tamanho da funda esticada
L = funda/2		#a funda deve ser dobrada no meio para seu uso, por isso seu valor é divido por dois
hLancamento = 1 #altura do lançamento em relação ao chão
g = 1 			#gravidade
diametro = 0.06	#diametro da pedra
aAngular = 1	#aceleração angular da mão
mao = 0.5 		#raio de rotação da mão

T = linspace(0,8,1001)		#tempo definido como 8 segundos

def rotacao(V,T):
	global sina,cosa
	global dxpdt,dypdt
	theta = (aAngular*T*T)/2 	#definição do angulo atual (em radianos) em função da aceleração angular e tempo 
	xm = mao * cos(theta)		#posição da mão no eixo x
	ym = mao * sin(theta)		#posição da mão no eixo y
	vxm = -mao * aAngular * T * sin(theta)	#velocidade da mão no eixo x
	vym = mao * aAngular * T * cos(theta)	#velocidade da mão no eixo y

	sina = (V[1]-ym)/L 			#seno do angulo atual formado entre a linha pedra-mão e o eixo x
	cosa = (V[0]-xm)/L 			#cosseno do mesmo angulo

	vmf = vxm * cosa + vym * sina	#conversão da velocidade da mão para o eixo f
	vpf = vmf	#velocidade da pedra é definida como a mesma na mão por estarem no eixo f
	vpp = 0 	#velocidade da pedra é 0 no eixo p por este ser definido como o tangente à pedra

	dxpdt = vpf * cosa 			#equação diferencial da velocidade da pedra no eixo x que será integrada para obter o espaço
	dypdt = vpf * sina			#mesmo, mas para o eixo y
	
	return [dxpdt,dypdt]


#Os valores de seno e cosseno finais são tirados da função, por trigonometria, pode-se provar que o valor o seno de lançamento é -cos do momento, assim como o cosseno do lançamento é -sen do momento.

def lancamento(V,T):
	dxdt = dxpdt * 10
	dydt = (dypdt - g*(T))*10

	return dxdt,dydt

M0 = [mao,-1*L]

L0 = [0,hLancamento]
t = linspace(0,5.15,101)

M = odeint(rotacao,M0,T)
L = odeint(lancamento,L0,t)		#o valor da rotação retornado é como se fosse uma corda sozinha, sem adicionar o valor da mão


for i in range(len(M[:,1])):
	M[:,0][i]+=mao
	M[:,1][i]+=mao

plt.title('Rotação')
plt.plot(M[:,0],M[:,1],'g')
plt.show()

plt.title('Lançamento')
plt.plot(L[:,0],L[:,1],'r')
plt.show()

# plt.title('SERÁ??!')
# plt.plot(S[0],S[1],'b')
# plt.show()