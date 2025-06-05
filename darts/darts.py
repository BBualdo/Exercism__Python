def score(x, y):
    # (x-a)^2 + (y-b)^2 = r^2
    if x**2 + y**2 <= 1**2:
        return 10
    elif x**2 + y**2 <= 5**2:
        return 5
    elif x**2 + y**2 <= 10**2:
        return 1
    else:
        return 0
