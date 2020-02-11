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
