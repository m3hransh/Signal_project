
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
