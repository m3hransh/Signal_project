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
