import numpy as np
import math
from sympy import *
init_printing()
q1,q2,q3,q4 = symbols('q1 q2 q3 q4', real=True)
links = 5;
a = np.array([0,0,0,0,5])
alpha = np.array([math.pi/2,math.pi/2,0,math.pi/2,math.pi/2])
d = np.array([0,0,5,5,0])
theta = np.array([pi,(-pi/2)+q1,q2,pi+q3,(pi/2)+q4])
def fk_calculate(links,a,alpha,d,theta):
	F = eye(4,4)
	for i in range(0,links):
		#h = np.array([[1,2,3],[4,5,6],[7,8,9]])
		#print(theta[1])
		T= Matrix([[cos(theta[i]),-sin(theta[i])*math.cos(alpha[i]),sin(theta[i])*math.sin(alpha[i]),a[i]*cos(theta[i])],
                    [sin(theta[i]),cos(theta[i])*math.cos(alpha[i]),-cos(theta[i])*math.sin(alpha[i]),a[i]*sin(theta[i])],
                    [0,math.sin(alpha[i]),math.cos(alpha[i]),d[i]],
                    [0,0,0,1]])
		#print(F.multiply(T))  
		F = F*T
		#pprint(F)
	return F[0:3,3]

Q = [q1,q2,q3,q4]
J = zeros(3,4)
#pprint(J)
F = fk_calculate(links,a,alpha,d,theta)
for j in range(0,3):
	for i in range (0,links-1):
		J[j,i] = diff(F[j],Q[i])
	#print (F[j],Q[i])
#pprint(J)
#pprint(simplify(F))
#print(F,'\n',J)
Jt = simplify(J[0:3,0:3])
pprint(simplify(Jt.det()))
#pprint(simplify(Jt))
