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

# %% 
#section:unit_step
def unit(x):
    return np.array([0 if i<0 else 1 for i in x ])
#endsection

# %%
#section:ramp
def ramp(x):
    return np.array([0 if i<0 else i for i in x])
#endsection

# #section:impulse
# def impulse(t,start,end,step):
#     result= np.zeros_like(t)
#     dt= (end-start)/step
#     n =int((0 - start)//dt)
#     if [n]==0:
#         v = 1/(t[n+1]-t[n-1])
#         result[n]=v
#         result[n-1] = v
#         result[n+1] = v
#     else:
#         v = 1/(t[n+1]-t[n])
#         result[n] = v
#         result[n+1] = v
        
#     return result
# #endsection
#%%
##section:Q1_1_delta
# t1 = np.linspace(-10,10,200)
# u = impulse(t1,-10,10,200)
# fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,5))
# ax1.plot(t1,u)
# ax1.set_xlabel('t')
# ax1.set_ylabel(r'$x(t)$')
# ax1.set_title(r'$\delta (t)$ with sampling rate of $F_s=100$')
# t2 = np.linspace(-10,10,2000)
# u = impulse(t2,-10,10,2000)
# ax2.plot(t2,u)
# ax2.set_xlabel('t')
# ax2.set_ylabel(r'$x(t)$')
# ax2.set_title(r'$\delta (t)$ with sampling rate of $F_s=1000$')
# plt.savefig('doc/images/Q1-1-delta.pgf')
# fig.show()
# #endsection
#%%
#section:Q1_1_unit
# create a figure with two axes in a row
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,5))
#sampling with rate of 10
t1= np.linspace(-10,10,200)
u = unit(t1)
ax1.plot(t1,u)
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$u(t)$ with sampling rate of $F_s=100$')

#sampling with rate of 100
t2 = np.linspace(-10,10,2000)
u2 = unit(t2)
ax2.plot(t2,u2)
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$u(t)$ with sampling rate of $F_s=1000$')
plt.savefig('doc/images/Q1-1-unit.pgf')
fig.show()
#endsection


# %%
#section:Q1_1_ramp
# create a figure with two axes in a row
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,5))

#sampling with rate of 10
t1= np.linspace(-10,10,200)
u = ramp(t1)
ax1.plot(t1,u)
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$r(t)$ with sampling rate of $F_s=100$')

#samping with rate of 100
t2 = np.linspace(-10,10,2000)
u2 = ramp(t2)
ax2.plot(t2,u2)
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$r(t)$ with sampling rate of $F_s=1000$')
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
