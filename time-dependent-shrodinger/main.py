import numpy as np
import matplotlib.pyplot as plt

L=6
V=-1
ep1=2
#t from 0 to 20


# initialising the H0 operator, should have V as a value on both ofset diagonals as in (12)
H0 = np.zeros((L, L))

for i in range(L):
    if i+1<=L-1:
        H0[i, i+1]=V
    if i-1>=0:
        H0[i, i-1]=V

#print(H0)
#print('\n')

# initialising the hamiltonian for times larger than 0
# H1 is just the value eps1 on the the site (0,0)
# H is H0 + H1
H1 = np.zeros((L,L))

H1[0,0]=ep1

H=H0 + H1

#print(H)H1[0,0]=ep1H1[0,0]=ep1
eig=np.linalg.eig(H0)
eigVal=eig.eigenvalues
eigVec=eig.eigenvectors
print(eigVec)

E0idx=np.where(eigVal==min(eigVal))
E0vec=eigVec[E0idx][0]
#print(E0vec)
print('\n')
print(eig)
print(eigVec[0])
t=0
Psi0 = np.empty((0))
for n in range(L):
    psi=0+0j
    for i in range(L):
        tempPsi=np.exp(-eigVal[i]*t*1j)*eigVec[i][n]
        tempPsi2=0
        for k in range(L):
            tempPsi2=tempPsi2 + eigVec[i][k]*eigVec[0][n]
        psi=psi+tempPsi*tempPsi2
    print(psi)
    Psi0=np.append(Psi0, [psi], 0)
    print(Psi0)

print('\n')
sum=0
for i in range(len(Psi0)):
    sum=sum+Psi0[i]**2
print(sum)
print(Psi0)


Psi0=Psi0*Psi0
x=np.arange(0, 6)
plt.plot(x, Psi0)
plt.show()