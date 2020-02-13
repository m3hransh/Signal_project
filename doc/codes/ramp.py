def ramp(x):
    if isinstance(x,Iterable):
        return np.array([0 if i<0 else i for i in x])
    else:
        return 0 if x<0 else x
