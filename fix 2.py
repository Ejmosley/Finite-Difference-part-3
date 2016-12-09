︠964c9c41-3dca-48a5-b126-938ff1e4ede1s︠
import scipy.special
import numpy as np
import scipy.linalg
#import numpy matrix
#from np import matrix
#from numpy import zeros
#from scipy import linalg

#PARAMETERS
h=20
k=12
th=0.01
r1=0.10
r2=0.47
r2c=(r2+(th/2))
L=(r2-r1)
Lc=(L+(th/2))
T1=100
Tinf=20

#EQUATIONS
m=(sqrt((2*h)/(12*th)))
Ab=(pi*(r1)^2)
Af=(2*pi*(((r2c)^2)-(r1)^2))
Ap=(Lc*th)
C2=(((2*r1)/(m))/(((r2c)^2)-(r1)^2))

#BESSEL FUNCTIONS
k0=scipy.special.k0(m*r1)
k1=scipy.special.k1(m*r1)
k1c=scipy.special.k1(m*r2c)
I0=scipy.special.i0(m*r1)
I1=scipy.special.i1(m*r1)
I1c=scipy.special.i1(m*r2c)

#FIN EFFICIENCY AND EFFECTIVENESS
eta=((C2*(((k1*I1c)-(I1*k1c))/((I0*k1c)+(k0*I1c))))) #EFFICIENCY
show("Fin efficiency is: {0:%}".format(eta,digits=8))

#show(r2c/r1) #LINE TO FOLLOW ON EFFICIENCY V.S. PSI PLOT
#xi=(((Lc)^(1.5))*(sqrt((h)/(k*Ap)))) #PSI
#show(xi)

EFFCT=((Af/Ab)*eta) #EFFECTIVENESS
show("Fin effectiveness is: {0:1}".format(EFFCT))

#EFFCTO=((h*(Ab+(eta*Af)*(T1-Tinf)/(h*Ab*(T1-Tinf))))) #OVERALL EFFECTIVENESS
#show(EFFCTO)

#FDM2
N=input ('Enter the number of unknowns (N) for problem:');
dr=L/N
dr2=dr*dr
r=r1+(L/N)

u=np.zeros(N)
A=np.zeros([N,N])
b=np.zeros(N-1)

for i in range(1,N-1):
    A[i,i-1]=1-(dr/(2*r[i]))
    A[i,i]=-(2+((m*m)*dr2))
    A[i,i+1]=1+(dr/(2*r[i]))
#BC 1
A[0,0]=1
b[0]=T1

#BC2
A[N-1,N-1]=1
A[N-1,N-2]=-1
b[N-1]=0

#Solution
u[:]=scipy.linalg.solve(A,b)+Tinf





#(numpy.zeros(shape=(N,N)))
#(numpy.zeros(shape=(N,0)))

#A=(numpy.zeros(shape=(N-1)))
#b=(numpy.zeros(shape=(N-1,1)))
#A[0,0]=(-(2+(m^2)*dr2))
#A(0,1)=1
#b(0)=(-(m^2)*(dr2)*Tinf)-T1
#A[0,0]=A[N,N]=1

#for i in range(2,N-2):
    #   A[i,i]=-(2+(m^2)*dr2)
     # A[i,i-1]=1
           # A[i,i+1]=1
    #b[i]=-(m^2)*(dr2)*Tinf
#A(N-1,N-1)=-((m^2)*(dr2)+1)
#A(N-1,N-2)=1
#b(N-1)=-((m*m)*(dr*dr)*Tinf)
#solution=scipy.linalg.solve(A,b)
#print solution
︡e1f54951-fa6a-4c91-b072-cce7228ca546︡{"html":"<div align='center'>Fin efficiency is: 6.340996%</div>"}︡{"html":"<div align='center'>Fin effectiveness is: 2.73455443047361</div>"}︡{"raw_input":{"prompt":"Enter the number of unknowns (N) for problem:"}}︡{"delete_last":true}︡{"raw_input":{"prompt":"Enter the number of unknowns (N) for problem:","submitted":true,"value":"5"}}︡{"stderr":"Error in lines 36-39\nTraceback (most recent call last):\n  File \"/projects/sage/sage-7.3/local/lib/python2.7/site-packages/smc_sagews/sage_server.py\", line 968, in execute\n    exec compile(block+'\\n', '', 'single') in namespace, locals\n  File \"\", line 2, in <module>\n  File \"sage/structure/element.pyx\", line 1859, in sage.structure.element.RingElement.__div__ (/projects/sage/sage-7.3/src/build/cythonized/sage/structure/element.c:16226)\n    return coercion_model.bin_op(self, right, div)\n  File \"sage/structure/coerce.pyx\", line 1091, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (/projects/sage/sage-7.3/src/build/cythonized/sage/structure/coerce.c:9974)\n    raise TypeError(arith_error_message(x,y,op))\nTypeError: unsupported operand parent(s) for '/': 'Real Field with 53 bits of precision' and '<type 'list'>'\n"}︡{"done":true}︡
︠e184664c-6a7e-439c-ae1f-944576aff787︠









