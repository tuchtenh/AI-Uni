import numpy as np
import matplotlib
import matplotlib.pyplot as plt


A = np.array([])
B = np.array([])

data = np.loadtxt('Data_Task_3.csv',skiprows=1, delimiter=';',dtype='str')
counter = 0
for line in data:
    counter += 1
    if counter % 2 == 0:
        x = (np.char.split(line, sep=','))
        for i in x:
            B = np.append(B, np.asfarray(i))
    else:
        x = (np.char.split(line, sep=','))
        for i in x:
            A = np.append(A, np.asfarray(i))


A = np.reshape(A,(-1,100))
B = np.reshape(B,(-1,100))

C = np.matmul(A, B)
plt.plot(C[0:5], 'ro')
plt.show()

