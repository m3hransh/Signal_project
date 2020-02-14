# return a convolution of function x1, x2 as an function
conv = lambda x1,x2: lambda n:np.array([sum([x1(k) * x2(i-k) for k in n])for i in n])
