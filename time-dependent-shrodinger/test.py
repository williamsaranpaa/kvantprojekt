import numpy as np

L=3**2
V=1

start=np.identity(L)
H=np.zeros((L, L))
for i in range(3):
    for j in range(2):
        H=H+V*(np.outer(start[i*3+j, :], start[:, i*3+j+1])+np.outer(start[i*3+j+1, :], start[:, i*3+j]))
for i in range(2):
    for j in range(3):
        H=H+V*(np.outer(start[i*3+j, :], start[:, (i+1)*3+j])+np.outer(start[(i+1)*3+j, :], start[:, i*3+j]))

print(H)