# Reactor Design Question (evaluated reactor height)
# âða =(ð1ð¶a)/(1+ð2ð¶a+ð3ð¶b)
# ð§= ð¶aoðâ«1/(âða)ðð¥ã
# Make a table and graph which shows z and x in the range of:  0â¤xâ¤0.9
# if you have function you can use quad
# if you have dataset

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

#Data
CA0 = 0.2
CB0 = 0
U = 7.5
k1=8
k2=3
k3=0.01
xspan = np.linspace(0,0.9,50)
zstore = np.zeros(len(xspan))

def myfun(X,k1,k2,k3,CA0,CB0,U):
    CA = CA0*(1-X)
    CB = CB0*(1+X)
    rA = k1*CA/(1+k2*CA+k3*CB)
    F = CA0*U/rA
    return F
    
for i in range(0,len(xspan)):
    x = xspan[i]
    z = quad(myfun,0,x,args=(k1,k2,k3,CA0,CB0,U))
    zstore[i] = z[0]



#plotting
x = zstore
y = xspan

plt.plot(x,y,'go--', linewidth=1, markersize=4)
plt.grid()
plt.xlabel('Height of reactor')
plt.ylabel('Conversion')