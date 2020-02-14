fig, ax = plt.subplots(1,1)

t = np.linspace(-4,2,1000)
# Definition of the x(t) signal as a lambda function
x = lambda t : -ramp(t+2) *unit(-t-1) +\
               (ramp(2*t+2)-1) * (unit(t+1)-unit(t)) +\
               unit(t) - unit(t-2)
# Shifting x(t) to the left and compress it
y = lambda t:x(2*t+2)
ax.plot(t,y(t))
ax.set_xlabel('t')
ax.set_ylabel(r'$y(t)$')
ax.set_yticks(np.arange(-1,2,step=1))

plt.savefig('doc/images/Q1-3-ex2.pgf')
fig.show()
