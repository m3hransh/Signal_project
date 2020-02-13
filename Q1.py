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

# %% 
#section:unit_step
def unit(x):
    # To support scalar values
    if isinstance(x, Iterable):
        return np.array([int(i>=0) for i in x ])
    else:
        return int(x>=0)
#endsection

# %%
#section:ramp
def ramp(x):
    if isinstance(x,Iterable):
        return np.array([0 if i<0 else i for i in x])
    else:
        return 0 if x<0 else x
#endsection

#%%
#section:Q1_1_unit
# create a figure with two axes in a row
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(11,5))
#sampling with rate of 10
t1= np.linspace(-5,5,100)
u = unit(t1)
ax1.plot(t1,u,'.-')
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$u(t)$ with sampling rate of $F_s=10$')

#sampling with rate of 100
t2 = np.linspace(-5,5,1000)
u2 = unit(t2)
ax2.plot(t2,u2,'.-')
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$u(t)$ with sampling rate of $F_s=100$')
plt.subplots_adjust(hspace=0.5)
fig.savefig('doc/images/Q1-1-unit.pgf')
fig.show()
#endsection


# %%
#section:Q1_1_ramp
# create a figure with two axes in a row
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(11,5))

#sampling with rate of 10
t1= np.linspace(-5,5,100)
u = ramp(t1)
ax1.plot(t1,u,'.-')
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$r(t)$ with sampling rate of $F_s=10$')

#samping with rate of 100
t2 = np.linspace(-5,5,1000)
u2 = ramp(t2)
ax2.plot(t2,u2,'.-')
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$r(t)$ with sampling rate of $F_s=100$')
plt.subplots_adjust(hspace=0.5)
plt.savefig('doc/images/Q1-1-ramp.pgf')
fig.show()
#endsection


# %%
#section:Q1_2_ex1
# create grid for the figure
gridsize = (3, 3)
fig = plt.figure(figsize=(16,11))
# The main siganl is on the right with two column to make it bigger
ax = plt.subplot2grid(gridsize, (0,1), rowspan=3,colspan=2)
ax1 = plt.subplot2grid(gridsize, (0,0))
ax2 = plt.subplot2grid(gridsize,(1,0))
ax3 = plt.subplot2grid(gridsize, (2,0))

# Sampling with the rate 8/1000
t= np.linspace(-4,4,1000)
# Parts of function
x1 = -ramp(t+2) *unit(-t-1)
x2 = (ramp(2*t+2)-1) * (unit(t+1)-unit(t))
x3 = unit(t) - unit(t-2)
x = x1+x2+x3

# Plotting first part
ax1.plot(t,x1)
ax1.set_title(r'$x_1(t)$')
ax1.set_xticks(np.arange(-4,4,step=1))

# Plotting second part 
ax2.plot(t,x2)
ax2.set_title(r'$x_2(t)$')
ax2.set_xticks(np.arange(-4,4,step=1))

# Plotting third part
ax3.plot(t,x3)
ax3.set_title(r'$x_3(t)$')
ax3.set_xticks(np.arange(-4,4,step=1))

# Plotting the full signal
ax.plot(t,x)
ax.set_xlabel('t')
ax.set_yticks(np.arange(-1,2,step=1))
ax.set_title(r'$x(t) = x_1(t) + x_2(t) + x_3(t)$')
ax.set_xticks(np.arange(-4,4,step=1))

plt.savefig('doc/images/Q1-2-ex1.pgf')
fig.show()
#endsection

# %%
#section:Q1_3_ex2
fig, ax = plt.subplots(1,1)

t = np.linspace(-4,2,1000)
# Definition of the x(t) signal as a lambda function
x = lambda t : -ramp(t+2) *unit(-t-1) +\
               (ramp(2*t+2)-1) * (unit(t+1)-unit(t)) +\
               unit(t) - unit(t-2)
# Shifting x(t) to the left and compress it
y = x(2*t+2)
ax.plot(t,y)
ax.set_xlabel('t')
ax.set_ylabel(r'$y(t)$')
ax.set_yticks(np.arange(-1,2,step=1))

plt.savefig('doc/images/Q1-3-ex2.pgf')
fig.show()
#endsection

# %%
#section:Q1_4_ex3
fig, ax = plt.subplots(1,1)

t = np.linspace(-3,4,1000)
# Definition of the x(t) signal as a lambda function
x = lambda t : -ramp(t+2) *unit(-t-1) +\
               (ramp(2*t+2)-1) * (unit(t+1)-unit(t)) +\
               unit(t) - unit(t-2)
# Shifting x(t) to the left and mirror it
y2 = x(-t+1)
ax.plot(t,y2)
ax.set_xlabel('t')
ax.set_ylabel(r'$y_2(t)$')
ax.set_yticks(np.arange(-1,2,step=1))

plt.savefig('doc/images/Q1-4-ex3.pgf')
fig.show()
#endsection


# %%
