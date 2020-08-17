x = 6
def f(x) :
    return x*x+2*x
def df(x):
    return 2*x+1
for i in range(100000):
    if abs(f(x))<1e-5:
        print(x, f(x))
        break
    elif f(x) > 0:
        x -= df(x) * 1e-4
    elif f(x) < 0:
        x += df(x) * 1e-4