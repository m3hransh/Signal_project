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
def unit_step(x):
    return [0 if i<0 else 1 for i in x ]
#endsection

#section:impulse
def impulse(t,start,end,step):
    result= np.zeros_like(t)
    dt= (end-start)/step
    n =int((0 - start)//dt)
    if [n]==0:
        v = 1/(t[n+1]-t[n-1])
        result[n]=v
        result[n-1] = v
        result[n+1] = v
    else:
        v = 1/(t[n+1]-t[n])
        result[n] = v
        result[n+1] = v
        
    return result
#endsection
#%%
#section:Q1_1_delta
t1 = np.linspace(-10,10,200)
u = impulse(t1,-10,10,200)
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,5))
ax1.plot(t1,u)
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$\delta (t)$ with sampling rate of $F_s=100$')
t2 = np.linspace(-10,10,2000)
u = impulse(t2,-10,10,2000)
ax2.plot(t2,u)
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$\delta (t)$ with sampling rate of $F_s=1000$')
plt.savefig('doc/images/Q1-1-delta.pgf')
fig.show()
#endsection
#%%
#section:Q1_1_unit
t1= np.linspace(-10,10,200)
u = unit_step(t1)
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(11,5))
ax1.plot(t1,u)
ax1.set_xlabel('t')
ax1.set_ylabel(r'$x(t)$')
ax1.set_title(r'$u(t)$ with sampling rate of $F_s=100$')
t2 = np.linspace(-10,10,2000)
u2 = unit_step(t2)
ax2.plot(t2,u2)
ax2.set_xlabel('t')
ax2.set_ylabel(r'$x(t)$')
ax2.set_title(r'$u(t)$ with sampling rate of $F_s=1000$')
plt.savefig('doc/images/Q1-1-unit.pgf')
fig.show()
#endsection




# %%
