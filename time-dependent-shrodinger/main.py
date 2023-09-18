import numpy as np


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

print(H0)
print('\n')

# initialising the hamiltonian for times larger than 0
# H1 is just the value eps1 on the the site (0,0)
# H is H0 + H1
H1 = np.zeros((L,L))

H1[0,0]=ep1

H=H0 + H1

#print(H)

print(np.linalg.eig(H0))

