from Q1 import x,y,y2
# d is the distance between samples
ct_energy = lambda x, n, d: sum([np.abs(x(i))**2 for i in n])*d

d = .0001
n = np.arange(-4,4,d)
x_en = ct_energy(x,n,d)
y1_en = ct_energy(y, n,d)
y2_en = ct_energy(y2,n,d)
