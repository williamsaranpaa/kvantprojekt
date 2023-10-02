import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

L=3**2      #Chosen Accuracyalla of the simulation,^2 for the dubbel elctorn condition.
V=-1        
ep1=-15     #might be 5 later
eps=0       #on site energies, 0 for all exept first
U1=0        #interference, fro n=1
U=15        #interference for all els

#t from 0 to 20


# initialising the H0 operator, should have V as a value on both ofset diagonals as in (12)
H0 = np.zeros((L, L))

for i in range(L):
    
    if i+1<=L-1:        #add V to diagnoal off center  
        H0[i, i+1]=V
    if i-1>=0:
        H0[i, i-1]=V
    if i-3>=0:
        H0[i-3][i]=V
    if i+3<L:
        H0[i+3][i]=V
    
    if(i<np.sqrt(L)):   #add the onsite energies
        if(i==0):
            H0[i][i]=2*ep1
        else:
            H0[i][i]=ep1
    else:
        if(i%np.sqrt(L)==0):    #"remove" V befre line
            H0[i][i]=ep1
            if(i-1!=0):
                H0[i-1][i]=0
                H0[i][i-1]=0

       
#print(H0)
#print('\n')

# initialising the hamiltonian for times larger than 0
# H1 is just the value eps1 on the the site (0,0)
# H is H0 + H1
print(H0)
H1 = np.zeros((L,L))

H1[0,0]=ep1

H=H0 + H1

#print(H)H1[0,0]=ep1H1[0,0]=ep1
eig1=np.linalg.eig(H0)
eigVal1=eig1.eigenvalues
eigVec1=eig1.eigenvectors
eig2=np.linalg.eig(H)
eigVal2=eig2.eigenvalues
eigVec2=eig2.eigenvectors
#print(eigVec)

#E0idx=np.where(eigVal==min(eigVal))
#E0vec=eigVec[E0idx][0]
#print(E0vec)
# print('\n')
# print(eig)
# print(eigVec[0])

Psi=np.zeros((20, 6), dtype=np.cfloat)
PsiN=np.zeros((6), dtype=np.cfloat)
#Psi0 = np.empty((0))
for t in range(20):
    if t==0:
        eigVal=eigVal1
        eigVec=eigVec1
    else:
        eigVal=eigVal2
        eigVec=eigVec2
    for n in range(L):
        psi=0+0j
        for i in range(L):
            tempPsi=np.exp(-eigVal[i]*t*1j)*eigVec[i][n]
            tempPsi2=0
            for k in range(L):
                tempPsi2=tempPsi2 + eigVec[i][k]*eigVec[0][k]
            psi=psi+tempPsi*tempPsi2
    #print(psi)
        PsiN[n]=psi
    Psi[t]=PsiN
    #print(Psi0)

print('\n')
print(Psi)
#print(Psi.ndim)
    #animate(t, Psi)

psiN=np.square(np.absolute(Psi))
print(psiN)
x=np.arange(0,6)
t= np.arange(0,20)
#psin=Psi[t, :]
ax = plt.axes(projection ='3d')

ax.contour3D(x, t, psiN, 50)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('|psi|²')
ax.set_title('probability distribution change')
#plt.plot(x, np.square(np.cos(x*np.pi/6))*(2/np.sqrt(6)))
plt.show()

# for t in range(20):
#     psiN=np.square(np.absolute(Psi[t]))
# # Psi0=np.square(np.absolute(Psi0))
#     x=np.arange(0,6)
# # x=np.arange(0, 6)
#     plt.plot(x, psiN)
#     plt.show()
#     print('done')
#     time.sleep(0.5)
#     plt.cla()


