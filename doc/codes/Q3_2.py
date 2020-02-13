# y1(t)
y1 = y(x1)
# y2(t)
y2 = y(lambda t: x1(t-3))

n = np.linspace(-5,5,1000)

fig, (ax1,ax2) = plt.subplots(1,2,figsize=(12,6))

ax1.plot(n, y1(n-3))
ax2.plot(n, y2(n))
fig.show()
