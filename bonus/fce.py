from matplotlib import pyplot as plt
import math

x = []
y = []
for i in range(1, 1000):
    num = i / 100
    x.append(num)
    y.append(math.log(num, math.e))

plt.plot(x, y)
plt.show()
