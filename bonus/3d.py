from vpython import *

krychle = box(pos=vector(0, 0, 0), length=1, color=color.blue)
koule = sphere(pos=vector(2, 0, 0), radius=0.5, color=color.green)
v = vector(0, 0, 0)
g = vector(0, -0.001, 0)

while True:
    rate(60)
    v += g
    koule.pos += v
    if koule.pos.y < -1:
        v.y *= -1