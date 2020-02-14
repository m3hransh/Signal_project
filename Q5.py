# %%
import numpy as np  
import matplotlib.pyplot as plt 
from collections.abc import Iterable


def unit(x):
    # To support scalar values
    if isinstance(x, Iterable):
        return np.array([int(i>=0) for i in x ])
    else:
        return int(x>=0)

def ramp(x):
    if isinstance(x,Iterable):
        return np.array([0 if i<0 else i for i in x])
    else:
        return 0 if x<0 else x

# %%
#section:Q5_1
# return a convolution of function x1, x2 as an function
conv = lambda x1,x2: lambda n:np.array([sum([x1(k) * x2(i-k) for k in n])for i in n])
#endsection
#section:Q5_2
x1 = lambda n :(2.0)**(n-1) * unit(n)
s = lambda i: sum([(np.sin(2*k)+ np.exp(2j*np.pi*k/2))*(unit(k+3)-unit(k-5))\
                   for k in range(-3,i+1)])
x2 = lambda n : np.array([s(i) if i <7 and i>0 else 0 for i in n ])\
                 if isinstance(n,Iterable) else (s(n) if n <7 and n>0 else 0)
x3 = conv(x1,x2)

n=np.arange(-3,20,1)
gridsize = (2,2)
fig =plt.figure(figsize=(16,11))
ax1 = plt.subplot2grid(gridsize,(0,0))
ax2 = plt.subplot2grid(gridsize,(0,1))
ax3 = plt.subplot2grid(gridsize,(1,0),colspan=2)

ax1.stem(n,x1(n),use_line_collection=True)
ax2.stem(n,x2(n).real,use_line_collection=True)
ax3.stem(n, x3(n).real,use_line_collection=True)

fig.show()
#endsection
plt.savefig('doc/images/Q5-2.pgf')
# %%
