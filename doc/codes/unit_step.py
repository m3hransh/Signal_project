def unit(x):
    # To support scalar values
    if isinstance(x, Iterable):
        return np.array([int(i>=0) for i in x ])
    else:
        return int(x>=0)
