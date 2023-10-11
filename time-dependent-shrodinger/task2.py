import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

L=6**2      #Chosen Accuracy of the simulation,^2 for the dubbel elctorn condition.
l=6
Time=np.arange(0, 20, 20/1000)
T=len(Time)
V=-1        
ep0=-15     #-15
eps=15       #on site energies, 0 for all exept first which is 5/15
U1=0        #interference, fro n=1
U=15        #interference for all els, 15

#t from 0 to 20


# initialising the H0 operator, should have V as a value on both ofset diagonals as in (12)
H0 = np.zeros((L, L))
start=np.identity(L)
for i in range(l):
    for j in range(l-1):
        H0=H0+V*(np.outer(start[i*l+j, :], start[:, i*l+j+1])+np.outer(start[i*l+j+1, :], start[:, i*l+j]))
        if i==j and i!=0:
            H0[l*i+j, l*i+j]=U
        if i==l-1 and j+1==i:
            H0[l*i+j+1, l*i+j+1]=U
for i in range(l-1):
    for j in range(l):
        H0=H0+V*(np.outer(start[i*l+j, :], start[:, (i+1)*l+j])+np.outer(start[(i+1)*l+j, :], start[:, i*l+j]))
#


for i in range(L):
    if i<l:   #add  the onsite energies
        if(i==0):
            H0[i][i]=2*ep0
        else:
            H0[i][i]=ep0
        #print(i)
    else:
        if(i%l==0):    
            H0[i][i]=ep0
            #print(f'later sites:{i}')
            
H = np.zeros((L, L))
start=np.identity(L)
for i in range(l):
    for j in range(l-1):
        H=H+V*(np.outer(start[i*l+j, :], start[:, i*l+j+1])+np.outer(start[i*l+j+1, :], start[:, i*l+j]))
        if i==j and i!=0:
            H[l*i+j, l*i+j]=U
        if i==l-1 and j+1==i:
            H[l*i+j+1, l*i+j+1]=U
for i in range(l-1):
    for j in range(l):
        H=H+V*(np.outer(start[i*l+j, :], start[:, (i+1)*l+j])+np.outer(start[(i+1)*l+j, :], start[:, i*l+j]))
#



# initialising the H0 operator, should have V as a value on both ofset diagonals as in (12)


for i in range(L):

    if i<l:   #add the onsite energies
        if(i==0):
            H[i][i]=2*eps
        else:
            H[i][i]=eps
    else:
        if(i%l==0):    #"remove" V befre line
            H[i][i]=eps
            
    

       
# print(H0)
# print('\n')

# # initialising the hamiltonian for times larger than 0
# # H1 is just the value eps1 on the the site (0,0)
# # H is H0 + H1
# #print(H0)
# print(H)
# for i in range(L):
#     print(H[i, :]-H0[i, :])
# print(H-H0)


#print(H)H1[0,0]=ep1H1[0,0]=ep1
eig1=np.linalg.eig(H0)
eigVal1=eig1.eigenvalues
eigVec1=eig1.eigenvectors
eig2=np.linalg.eig(H)
eigVal2=eig2.eigenvalues
eigVec2=eig2.eigenvectors
#print(eigVec)
E0idx=np.where(eigVal1==min(eigVal1))
E0vec=eigVec1[:, E0idx[0][0]]

#E0idx=np.where(eigVal==min(eigVal))
#E0vec=eigVec[E0idx][0]
#print(E0vec)
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

psiN=np.square(np.absolute(Psi))





#Ploting the particle desity for 6 sites dependet on time.
plt.plot(Time, psiN[:, 0*l+0], color='r', label='site 1')
plt.plot(Time, psiN[:, l+1], color='b', label='site 2')
plt.plot(Time, psiN[:, 2*l+2], color='g', label='site 3')
plt.plot(Time, psiN[:, 3*l+3], color='c', label='site 4')
plt.plot(Time, psiN[:, 4*l+4], color='m', label='site 5')
plt.plot(Time, psiN[:, 5*l+5], color='y', label='ste 6')

# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Time")
plt.ylabel("|psi|²")
plt.title("Density in the different states dependent on time when the electrons are at the same site")
# psi1=np.sum(psiN[:, :6], axis=1)
# #print(psi1)
# print('\n')
# psi11=np.zeros(1000)
# for i in range(6):
#     psi11+=psiN[:, i]
# #print(psi11)
# print('\n')
# print(psi1-psi11)
# print(np.size(psi1))
# print(np.size(psi11))
#print(np.sum(psiN[:6, :], axis=1))

# #Ploting the particle desity for 6 sites dependet on time.
# plt.plot(Time, np.sum(psiN[:, :l], axis=1), color='r', label='site 1')
# plt.plot(Time, np.sum(psiN[:, l:2*l], axis=1), color='b', label='site 2')
# plt.plot(Time, np.sum(psiN[:, 2*l:3*l], axis=1), color='g', label='site 3')
# plt.plot(Time, np.sum(psiN[:, 3*l:4*l], axis=1), color='c', label='site 4')
# plt.plot(Time, np.sum(psiN[:, 4*l:5*l], axis=1), color='m', label='site 5')
# plt.plot(Time, np.sum(psiN[:, 5*l:], axis=1), color='y', label='ste 6')

# # Naming the x-axis, y-axis and the whole graph
# plt.xlabel("Time")
# plt.ylabel("|psi|²")
# plt.title("Density in the different states for the spin up electron dependent on time")
  
# # Adding legend, which helps us recognize the curve according to it's color
plt.legend()
# Displaying all plots
plt.show()

#psin=Psi[t, :]
# ax = plt.axes(projection ='3d')

# ax.contour3D(x, t, psiN, 100)
# ax.set_xlabel('x')
# ax.set_ylabel('t')
# ax.set_zlabel('|psi|²')
# ax.set_title('probability distribution change')
#plt.plot(x, np.square(np.cos(x*np.pi/6))*(2/np.sqrt(6)))


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


