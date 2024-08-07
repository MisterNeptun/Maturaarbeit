import numpy as np
import copy
x=np.array([[0.3, 0.4,0.1],
            [0.5, 0.2,0.3],
            [0.2, 0.4, 0.6]])
ew,ev=np.linalg.eig(x)
print(ew)
print(ev)
t=np.zeros([3,3])
for i in range(3):
    t[i][i]=ew[i]
print(np.matmul(np.matmul(np.matmul(ev,(t)),np.linalg.inv(ev)),[5000,0,5000]))

for i in range(3):
    if (1-t[i][i])>0.00000001:
        t[i][i]=0

print(t)

print(np.matmul(np.matmul(np.matmul(ev,t),np.linalg.inv(ev)),[5000,0,5000]))

w=np.matmul(np.matmul(np.matmul(ev,t),np.linalg.inv(ev)),[5000,0,5000])
w=w.tolist()
w.insert(1,1)
print(w)



y=copy.deepcopy(x)
for i in range(20000):
   y=copy.deepcopy(np.matmul(y,x))
print(np.matmul(y,x))

