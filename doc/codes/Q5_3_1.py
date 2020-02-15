# Definition of x[n]
xn = lambda n: np.cos(n**2) * np.sin(2*np.pi*n/5)
# Definition of h[n]
hn = lambda n: (.9)**n*(unit(n)- unit(n-10))
# Samples from 0 to 99
n = np.arange(0,100,1)
# Result vector of x(n) on n
x = xn(n)
# Sample for h[n]
n1 = np.arange(0,11,1)
h = hn(n1)
# Defining two block 
x0n = lambda n: np.array([xn(i) if i<50 and i >=0 else 0 for i in n])
x1n = lambda n: np.array([xn(i+50) if i<50 and i >=0 else 0 for i in n])
# Result of x0 and x1 on sample n
x0 = x0n(n)
x1 = x1n(n)
yn = np.convolve(x, h)
y0 = np.convolve(x0,h)
y1 = np.convolve(x1,h)
# Sample for convolution result that has n+m-1 samples
n2 = np.concatenate((n, np.arange(n[-1],n[-1]+n1.size-1,1)))
ypn = lambda t : np.array([y0[i]+y1[i-50] if x-50>=0 else y0[i] for i,x in enumerate(t) ])
yp = ypn(n2)
