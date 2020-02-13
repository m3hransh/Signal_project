#%%
import matplotlib
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# %%
import numpy as np  
import matplotlib.pyplot as plt 
from collections.abc import Iterable
from Q1 import x


# %%
#section:Q2_def

# Defintion of systems that take a signal x as an input and return siganl f 
fx_o = lambda x: lambda n:(x(n) - x(-n))/2
fx_e = lambda x: lambda n: (x(n) + x(-n))/2
fx_t = lambda x: lambda n: np.array([x(np.array([i]))[0] if i<0 else 0 for i in n])
fx_r = lambda x: lambda n: np.array([x(np.array([i]))[0] if i>=0 else 0 for i in n])

# Call them on the signal x(t)
x_o = fx_o(x)
x_e = fx_e(x)
x_t = fx_t(x)
x_r = fx_r(x)
#endsection

#section:Q2_1
# Sampling with rate of 100
n = np.linspace(-4,4,800)

# Making figure with 2 rows and 2 columns
gridsize = (2, 2)
fig = plt.figure(figsize=(16,11))
ax1 = plt.subplot2grid(gridsize, (0,0))
ax2 = plt.subplot2grid(gridsize, (0,1))
ax3 = plt.subplot2grid(gridsize,(1,0))
ax4 = plt.subplot2grid(gridsize, (1,1))

ax1.plot(n, x_o(n))
ax1.set_title(r'$x_o(n)$')
ax1.set_xticks(np.arange(-4,5,step=1))
ax1.set_yticks(np.arange(-1,1.5,step=.5))

ax2.plot(n, x_e(n))
ax2.set_title(r'$x_e(n)$')
ax2.set_xticks(np.arange(-4,5,step=1))
ax2.set_yticks(np.arange(-1,1.5,step=.5))

ax3.plot(n, x_t(n))
ax3.set_title(r'$x_t(n)$')
ax3.set_xticks(np.arange(-4,5,step=1))
ax3.set_yticks(np.arange(-1,1.5,step=.5))

ax4.plot(n, x_r(n))
ax4.set_title(r'$x_r(n)$')
ax4.set_xticks(np.arange(-4,5,step=1))
ax4.set_yticks(np.arange(-1,1.5,step=.5))

fig.show()
#endsection
plt.savefig('doc/images/Q2-1.pgf')

# %%
#section:Q2_2

fx_e = lambda x: lambda n: (x(n) + x(-n))/2
fx_r = lambda x: lambda n: np.array([x(np.array([i]))[0] if i>=0 else 0 for i in n])
x_e = fx_e(x)
x_r = fx_r(x)

# x(t) for t>=0
nx = lambda t: 2*x_e(t) - x_r(-t)
# The function concatenate the negetive part with positive
xg = lambda t: np.concatenate((nx(np.array([i for i in t if i<0])),x_r(np.array([i for i in t if i>=0]))))

# Sampling with rate of 100
t = np.linspace(-4,4,800)
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(16,6))

# Plotting original x(t)
ax1.plot(t, x(t))
ax1.set_title('original $x(t)$')
ax1.set_xticks(np.arange(-4,5,step=1))
ax1.set_yticks(np.arange(-1,1.5,step=.5))

# Plotting generated signal
ax2.plot(t, xg(t))
ax2.set_title('generated $x(t)$ using signals $x_r(t)$ and $x_e(t)$')
ax2.set_xticks(np.arange(-4,5,step=1))
ax2.set_yticks(np.arange(-1,1.5,step=.5))

fig.show()
#endsection
plt.savefig('doc/images/Q2-2.pgf')
