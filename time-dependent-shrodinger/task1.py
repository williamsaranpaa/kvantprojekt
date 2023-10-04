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
# Creating subplots
fig, (axs1, axs2, axs3, axs4, axs5, axs6) = plt.subplots(6, 1, figsize = (8, 7))

# Plotting of the first subplot
axs1.plot(Time, psiN[:, 0], 'r', label = 'Site 1')
axs1.set_xlabel('Time')
axs1.set_ylabel('|psi|² \n Site 1')     #Är detta nödvändigt?
axs1.legend()

# Plotting of the second subplot
axs2.plot(Time, psiN[:, 1], 'b', label = 'Site 2')
axs2.set_xlabel('Time')
axs2.set_ylabel('|psi|²')
axs2.legend()

# Plotting of the second subplot
axs3.plot(Time, psiN[:, 2], 'g', label = 'Site 3')
axs3.set_xlabel('Time')
axs3.set_ylabel('|psi|²')
axs3.legend()

# Plotting of the second subplot
axs4.plot(Time, psiN[:, 3], 'r', label = 'Site 4')
axs4.set_xlabel('Time')
axs4.set_ylabel('|psi|²')
axs4.legend()

# Plotting of the second subplot
axs5.plot(Time, psiN[:, 4], 'b', label = 'Site 5')
axs5.set_xlabel('Time')
axs5.set_ylabel('|psi|²')
axs5.legend()

# Plotting of the second subplot
axs6.plot(Time, psiN[:, 5], 'g', label = 'Site 6')
axs6.set_xlabel('Time')
axs6.set_ylabel('|psi|²')
axs6.legend()

# for adjusting the space between subplots
plt.tight_layout()
# Displaying all plots
plt.show()

#LIlly dum dum 
#: är allt A[0] =rade A[:, 0]=kolumen
# poltte A[:, n]=kolumen n = 0-->5 i olia sublot mot time
#plt.plot(Time, psiN[:, 0]) #det är detta js ska plotta i oloka subplots 


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


