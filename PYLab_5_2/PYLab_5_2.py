import numpy as np
import matplotlib.pyplot as plt

tn = 0      #Задано условием
tk = 10     #Задано условием
dt = 0.1    #Взято за пример

t = np.arange(tn, tk, dt)

S1 = 1.2 * np.cos(2 * t)
S2 = 1.5 * np.cos(2 * t)
S3 = np.array([])

for i in range(len(t)):
    if S1[i] < 0:
        S3 = np.append(S3, S1[i])
    if S2[i] < 0:
        S3 = np.append(S3, S2[i])

plt.subplot(131)
plt.title("Исходные сигналы")
plt.plot(t, S1)
plt.plot(t, S2)
plt.subplot(132)

t = t[:len(S3):]

plt.title("Рез-щий по критерию #1")
plt.plot(t, S3)

for i in range(len(t)):
    if S3[i] <= -0.5:
        S3[i] = -0.5

plt.subplot(133)
plt.title("Рез-щий по критерию #2")
plt.plot(t, S3)
plt.show()