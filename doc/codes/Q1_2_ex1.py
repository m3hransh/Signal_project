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
