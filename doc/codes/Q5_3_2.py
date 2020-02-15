# Plotting all siganls in Grid
gridsize = (6,2)
fig = plt.figure(figsize=(16,24))
plt.subplots_adjust(hspace=0.5)
ax1 = plt.subplot2grid(gridsize,(0,0),colspan=2)
ax2 = plt.subplot2grid(gridsize,(1,0))
ax3 = plt.subplot2grid(gridsize,(2,0))
ax4 = plt.subplot2grid(gridsize, (1,1),rowspan=2)
ax5 = plt.subplot2grid(gridsize,(3,0))
ax6 = plt.subplot2grid(gridsize,(3,1))
ax7 = plt.subplot2grid(gridsize,(4,0),colspan=2)
ax8 = plt.subplot2grid(gridsize,(5,0),colspan=2)

ax1.stem(n, x)
ax1.set_title(r'$x[n]$')

ax2.stem(n, x0)
ax2.set_title(r'$x_0[n]$')
ax2.set_xlim(0,50)

ax3.stem(n, x1)
ax3.set_title(r'$x_1[n]$')
ax3.set_xlim(0,50)

ax4.stem(n1, h)
ax4.set_title(r'$h[n]$')

ax5.stem(n2,y0,'g',markerfmt='go')
ax5.set_title(r'$y_0[n]$')
ax5.set_xlim(0,60)

ax6.stem(n2,y1,'r',markerfmt='ro')
ax6.set_title(r'$y_1[n]$')
ax6.set_xlim(0,60)

ax7.stem(n2,yp,label='$y_0[n]+y_1[n]$')
ax7.stem(n2,y0,'g',markerfmt='go',label='$y_0[n]$')
ax7.stem(n2+50,y1,'r',markerfmt='ro',label='$y_1[n-50]$')
ax7.set_xlim(0,110)
ax7.set_title(r'$y_0[n]+y_1[n]$')
ax7.legend()
ax8.stem(n2, np.convolve(x,h))
ax8.set_title(r'$x[n]*h[n]$')
