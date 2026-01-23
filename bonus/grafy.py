from matplotlib import pyplot as plt

znamky = [2, 4, 1, 2, 1, 1, 1, 1, 2, 1, 4, 1, 5]
x = []
y = []


s = 0
for i in range(len(znamky)):
    x.append(i)
    s += znamky[i]
    y.append(s / (i + 1))

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]

#plt.scatter(x, y)
plt.plot(x, y)
plt.plot(x2, y2)
plt.show()
