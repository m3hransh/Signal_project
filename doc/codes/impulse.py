def impulse(t,start,end,step):
    result= np.zeros_like(t)
    dt= (end-start)/step
    n =int((0 - start)//dt)
    if [n]==0:
        v = 1/(t[n+1]-t[n-1])
        result[n]=v
        result[n-1] = v
        result[n+1] = v
    else:
        v = 1/(t[n+1]-t[n])
        result[n] = v
        result[n+1] = v
        
    return result
