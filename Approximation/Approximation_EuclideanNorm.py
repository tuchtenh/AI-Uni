# TODO: add imports
import numpy as np
import matplotlib.pyplot as plt
import scipy

class RegressionModel:
    def __init__(self, degree):
        self.degree = degree
        self.model = None
        self.X = None

    #Aufgabe 3a
    def fit(self, x_train, y_train, num_iterations,tolerance, learningrate):
        # TODO: implement method to train model
        self.X = self._generate_features(x_train)
        X = self.X
        iteration=0
        n = len(x_train)
        print(np.size(X))
        w = np.zeros(self.degree + 1)
        grad = np.dot(np.matmul(np.transpose(X),X),w) - np.dot(np.transpose(y_train),X)
        while iteration <= num_iterations and np.linalg.norm(grad) > tolerance:
            w = w - learningrate*(1/n)*grad
            #print(w)
            grad = np.dot(np.matmul(np.transpose(X),X),w) - np.dot(np.transpose(y_train),X)
            iteration += 1
        self.model = w
        #print('todo: optimize model parameters')

    #Aufgabe 4
    def predict(self, x_test):
        # TODO: implement method to apply model
        if self.model is None:
            raise RuntimeError('fit a model using .fit(...) before calling .predict(...)')
        else:
            feat = self._generate_features(x_test)
            y_test = np.matmul(feat, self.model)
        return y_test
        #print('todo: return y_predict')

    #Aufgabe 2
    def _generate_features(self, x_values):
        # TODO: implement method to prepare values for X = [1, ... , x^degree]
        n = np.size(x_values)
        p = self.degree
        X = np.zeros((n, p+1))
        X[:,0] = np.ones(n)
        for i in range (1, p+1):
            X[:,i] = [np.power(x_values[j], i) for j in range(n)]
        return X


"""
#### example usage 
...
p2 = RegressionModel(2)
p2.fit(x_train, y_train)
y_predict = p2.predict(x_test)
...
"""
# Aufgabe 1
daten = np.loadtxt('Train_Dataset.csv')
x_train = daten[:,0]
y_train = daten[:,1]
n = sum(1 for row in daten)
print("n = ", n)

plt.scatter(x_train, y_train, marker=".")

#Aufgabe 3b
p2 = RegressionModel(2)
p3 = RegressionModel(3)
p4 = RegressionModel(4)

## tolerance, learningrate richtig eingeben
p2.fit(x_train, y_train,n, 10**(-5),10**(-10))
p3.fit(x_train, y_train,n, 10**(-5),10**(-19))
p4.fit(x_train, y_train,n, 10**(-5),10**(-24))

print(p2.model)
print(p3.model)
print(p4.model)
plt.plot(x_train, np.dot(p2.X,p2.model),color = 'r')
plt.plot(x_train, np.dot(p3.X,p3.model),color = 'g')
plt.plot(x_train, np.dot(p4.X,p4.model),color = 'm')
plt.show()

#Aufgabe 4 einlesen
test = np.loadtxt('Test_Dataset.csv')
x_test = test[:,0]
y_test = test[:,1]

nn = sum(1 for row in test)
print("nn = ", nn)

plt.scatter(x_test, y_test, marker=".")

#Aufgabe 4 predict
p22 = RegressionModel(2)
p33 = RegressionModel(3)
p44 = RegressionModel(4)

## tolerance, learningrate richtig eingeben
p22.fit(x_test, y_test,nn, 10**(-2),10**(-13))
p33.fit(x_test, y_test,nn, 10**(-2),10**(-19))
p44.fit(x_test, y_test,nn, 10**(-2),10**(-25))

#print(p2.model)
#print(p3.model)
#print(p4.model)
#plt.plot(x_test, np.dot(p2.X,p2.model),color = 'r')
#plt.plot(x_test, np.dot(p3.X,p3.model),color = 'g')
#plt.plot(x_test, np.dot(p4.X,p4.model),color = 'm')

plt.plot(p22.predict(x_test))
plt.plot(p33.predict(x_test))
plt.plot(p44.predict(x_test))
plt.show()



#Aufgabe 5
def ed(y,dy):
    y = np.array(y)
    cy = np.array(dy)
    sub = y - cy
    sq = sub**2
    sum = np.sum(sq)
    return np.sqrt(sum)

y1 = [0.8, 0.43, 1.74, 0.26, 4.06, 0.73, 2.8, 3.37]
y2 = [3.49, 1.3, 1.49, 4.12, 2.19, 4.24, 4.67, 0.22]
test = ed(y1,y2)
print(test)