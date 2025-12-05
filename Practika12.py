def taskA_1(a, b):
    def step(c, d):
        if d == 0:
            return 1
        return c * step(c, d - 1)

    def faktor(i):
        if i == 0:
            return 1
        return i * faktor(i - 1)

    return step(a, b) / faktor(b)

def taskB_1():
    h = int(input())
    if h == 0:
        return h
    r = taskB_1()
    return h if h > r else r

print(taskA_1(2, 3))
