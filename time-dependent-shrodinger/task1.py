import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

L=6
Time=np.arange(0, 20, 20/1000)
T=len(Time)
V=-1
ep1=-2
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
eig1=np.linalg.eig(H0)
eigVal1=eig1.eigenvalues
eigVec1=eig1.eigenvectors
eig2=np.linalg.eig(H)
eigVal2=eig2.eigenvalues
eigVec2=eig2.eigenvectors
#print(eigVec)
# print(H0)

# print(eigVal1)
# print('\n')
E0idx=np.where(eigVal1==min(eigVal1))
E0vec=eigVec1[:, E0idx[0][0]]
# print(eig1)
# print(E0idx[0][0])
# print('\n')
# print(np.square(E0vec))
# sum=0
# sum2=0
# for i in range(6):
#     sum +=E0vec[i]**2
#     sum2+=np.square(E0vec)[i]
# print(sum)
# print(sum2)
# print('\n')
# print(eig)
# print(eigVec[0])

Psi=np.zeros((T, L), dtype=np.cfloat)
PsiN=np.zeros((L), dtype=np.cfloat)
#Psi0 = np.empty((0))
for t in range(T):
    if t==0:
        eigVal=eigVal1
        eigVec=eigVec1
    else:
        eigVal=eigVal2
        eigVec=eigVec2
    for n in range(L):
        psi=0+0j
        for i in range(L):
            tempPsi=np.exp(-eigVal[i]*Time[t]*1j)*eigVec[n][i]
            tempPsi2=0
            for k in range(L):
                tempPsi2=tempPsi2 + eigVec[k][i]*E0vec[k]
            psi=psi+tempPsi*tempPsi2
    #print(psi)
        PsiN[n]=psi
    Psi[t]=PsiN
    #print(Psi0)

#print('\n')
#print(Psi)
#print(Psi.ndim)
    #animate(t, Psi)
#print(Time)
psiN=np.square(np.absolute(Psi))
#print(psiN)
x=np.arange(0,L)
#t= np.arange(0,T)
#print(np.shape(psiN))
#print(len(psiN[:,0]))
# plt.plot(x, np.square(E0vec))
# plt.show()

#Ploting the particle desity for 6 sites dependet on time.
plt.plot(Time, psiN[:, 0], color='r', label='site 1')
plt.plot(Time, psiN[:, 1], color='b', label='site 2')
plt.plot(Time, psiN[:, 2], color='g', label='site 3')
plt.plot(Time, psiN[:, 3], color='c', label='site 4')
plt.plot(Time, psiN[:, 4], color='m', label='site 5')
plt.plot(Time, psiN[:, 5], color='y', label='ste 6')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Time")
plt.ylabel("|psi|²")
plt.title("Density in the different states dependent on time")
  
# Adding legend, which helps us recognize the curve according to it's color
plt.legend()
# Displaying all plots
plt.show()


#####plt.plot(x, np.square(E0vec))

#psin=Psi[t, :]
# ax = plt.axes(projection ='3d')

# ax.contour3D(x, t, psiN, 50)
# ax.set_xlabel('x')
# ax.set_ylabel('t')
# ax.set_zlabel('|psi|²')
# ax.set_title('probability distribution change')
#plt.plot(x, np.square(np.cos(x*np.pi/6))*(2/np.sqrt(6)))
#plt.show()

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


