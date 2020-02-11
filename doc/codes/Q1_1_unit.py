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
