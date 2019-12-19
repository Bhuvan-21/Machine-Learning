def f(t0, t1, x):
    return t0+t1*x


def sum0(t0, t1, list0, m):
    val = 0
    for i in list0:
        val += (f(t0, t1, i[0]) - i[1])
    val = val / m
    return val


def sum1(t0, t1, list0, m):
    val = 0
    for i in list0:
        val += (f(t0, t1, i[0]) - i[1])*i[0]
    val = val / m
    return val


def j(t0, t1, list0, m):
    val = 0
    for i in list0:
        val += (f(t0, t1, i[0])-i[1])**2
    val = val/(2*m)
    return val


House_prices = []
n = 0
while True:
    n += 1
    area = float(input("Enter the area:"))
    cost = float(input("Enter the cost:"))
    df = [area, cost]
    House_prices.append(df)
    ans = input("Do you want to continue?(y/n)")
    if ans == "n":
        break
tt0 = 1
tt1 = 1
alpha = 0.01
while True:
    j0 = j(tt0, tt1, House_prices, n)
    temp1 = tt0 - alpha*sum0(tt0, tt1, House_prices, n)
    temp2 = tt1 - alpha*sum1(tt0, tt1, House_prices, n)
    tt0 = temp1
    tt1 = temp2
    j1 = j(tt0, tt1, House_prices, n)
    if abs(j1-j0) < 0.000001:
        break
while True:
    area = float(input("Enter area:"))
    print(f(tt0, tt1, area))
    ans = input("Enter n to stop:")
    if ans == "n":
        break
