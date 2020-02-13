
# Defintion of systems that take a signal x as an input and return siganl f 
fx_o = lambda x: lambda n:(x(n) - x(-n))/2
fx_e = lambda x: lambda n: (x(n) + x(-n))/2
fx_t = lambda x: lambda n: np.array([x(np.array([i]))[0] if i<0 else 0 for i in n])
fx_r = lambda x: lambda n: np.array([x(np.array([i]))[0] if i>=0 else 0 for i in n])

# Call them on the signal x(t)
x_o = fx_o(x)
x_e = fx_e(x)
x_t = fx_t(x)
x_r = fx_r(x)
