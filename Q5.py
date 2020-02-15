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
ax1.set_title("$x_1[n]$")
ax2.stem(n,x2(n).real,use_line_collection=True)
ax2.set_title("$|x_2[n]|$")
ax3.stem(n, x3(n).real,use_line_collection=True)
ax3.set_title('|x_1[n]*x_2[n]|')

fig.show()
#endsection
plt.savefig('doc/images/Q5-2.pgf')
# %%
#section:Q5_3_1
# Definition of x[n]
xn = lambda n: np.cos(n**2) * np.sin(2*np.pi*n/5)
# Definition of h[n]
hn = lambda n: (.9)**n*(unit(n)- unit(n-10))
# Samples from 0 to 99
n = np.arange(0,100,1)
# Result vector of x(n) on n
x = xn(n)
# Sample for h[n]
n1 = np.arange(0,11,1)
h = hn(n1)
# Defining two block 
x0n = lambda n: np.array([xn(i) if i<50 and i >=0 else 0 for i in n])
x1n = lambda n: np.array([xn(i+50) if i<50 and i >=0 else 0 for i in n])
# Result of x0 and x1 on sample n
x0 = x0n(n)
x1 = x1n(n)
yn = np.convolve(x, h)
y0 = np.convolve(x0,h)
y1 = np.convolve(x1,h)
# Sample for convolution result that has n+m-1 samples
n2 = np.concatenate((n, np.arange(n[-1],n[-1]+n1.size-1,1)))
ypn = lambda t : np.array([y0[i]+y1[i-50] if x-50>=0 else y0[i] for i,x in enumerate(t) ])
yp = ypn(n2)
#endsection
#section:Q5_3_2
# Plotting all siganls in Grid
gridsize = (6,2)
fig = plt.figure(figsize=(16,24))
plt.subplots_adjust(hspace=0.5)
ax1 = plt.subplot2grid(gridsize,(0,0),colspan=2)
ax2 = plt.subplot2grid(gridsize,(1,0))
ax3 = plt.subplot2grid(gridsize,(2,0))
ax4 = plt.subplot2grid(gridsize, (1,1),rowspan=2)
ax5 = plt.subplot2grid(gridsize,(3,0))
ax6 = plt.subplot2grid(gridsize,(3,1))
ax7 = plt.subplot2grid(gridsize,(4,0),colspan=2)
ax8 = plt.subplot2grid(gridsize,(5,0),colspan=2)

ax1.stem(n, x)
ax1.set_title(r'$x[n]$')

ax2.stem(n, x0)
ax2.set_title(r'$x_0[n]$')
ax2.set_xlim(0,50)

ax3.stem(n, x1)
ax3.set_title(r'$x_1[n]$')
ax3.set_xlim(0,50)

ax4.stem(n1, h)
ax4.set_title(r'$h[n]$')

ax5.stem(n2,y0,'g',markerfmt='go')
ax5.set_title(r'$y_0[n]$')
ax5.set_xlim(0,60)

ax6.stem(n2,y1,'r',markerfmt='ro')
ax6.set_title(r'$y_1[n]$')
ax6.set_xlim(0,60)

ax7.stem(n2,yp,label='$y_0[n]+y_1[n]$')
ax7.stem(n2,y0,'g',markerfmt='go',label='$y_0[n]$')
ax7.stem(n2+50,y1,'r',markerfmt='ro',label='$y_1[n-50]$')
ax7.set_xlim(0,110)
ax7.set_title(r'$y_0[n]+y_1[n]$')
ax7.legend()
ax8.stem(n2, np.convolve(x,h))
ax8.set_title(r'$x[n]*h[n]$')
#endsection
plt.savefig('doc/images/Q5-3.pgf')
# %%
