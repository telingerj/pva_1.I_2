from matplotlib import pyplot as plt
import random

x = []
y = []
s = 0
for i in range(10000000):
    x.append(i)
    num = random.randint(0, 1)
    if num == 0:
        s += 1
    else:
        s -= 1
    y.append(s)


plt.plot(x, y)
plt.show()
