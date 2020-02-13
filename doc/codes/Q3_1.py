# Defining the y(t) systems that takes signal as an input
y = lambda f: lambda t:np.array([integrate.quad(lambda u:f(u-2)*np.exp(u-i),-10,10)[0] for i in t])
x1 = lambda t: unit(t) - unit(t-2)
x2 = lambda t: unit(t) - unit(t-2)
a1=3
a2=2
# S{a1x1(t) + a2x2(t)}
y1 = y(lambda t: a1*x1(t)+a2*x2(t))
# S{a1x1(t)} + S{a2x2(t)}
y2 = lambda t1:y(lambda t: a1*x1(t))(t1)+ y(lambda t : a2*x1(t))(t1)
# Sampling with rate of 100
n = np.linspace(-5,5,1000)
# Making the figure with 2 axes in a row
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,6))

ax1.plot(n, y1(n))
ax2.plot(n, y2(n))
fig.show()
