import matplotlib.pyplot as plot
import random

randomX=[]
randomY=[]

for i in range(0, 30):
    n = random.randint(1, 30)
    m = random.randint(100, 400)
    randomX.append(n)
    randomY.append(m)

plot.hist(randomX)
# plot.scatter(randomX, randomY)
