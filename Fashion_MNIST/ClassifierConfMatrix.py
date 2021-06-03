import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

train_img = np.load("x_train.npy")
ytrain = np.load("y_train.npy")
test_img = np.load("x_test.npy")
ytest = np.load("y_test.npy")


train_img = np.array([elem.flatten() for elem in train_img], dtype=np.float)
train_img = np.array([elem.flatten() for elem in ytrain], dtype=np.float)
test_img = np.array([elem.flatten() for elem in test_img], dtype=np.float)
ytest_img = np.array([elem.flatten() for elem in ytest], dtype=np.float)


X_train, X_test, y_train, y_test = train_test_split(train_img, ytrain, test_size = 0.2, random_state = 123, shuffle = True)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


train_on_subset = False


#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128,64,32), learning_rate='adaptive', batch_size=16, learning_rate_init=0.001, max_iter=200, verbose=True)  # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64,32,16), learning_rate='adaptive', batch_size=8, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128,64,32), learning_rate='adaptive', batch_size=64, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="tanh", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128,64,32), learning_rate='adaptive', batch_size=8, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="logistic", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128,64,32), learning_rate='adaptive', batch_size=8, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256,128,64,32), learning_rate='adaptive', batch_size=16, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256,128,64,32), learning_rate='adaptive', batch_size=64, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256,128,32), learning_rate='adaptive', batch_size=64, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256,128,64), learning_rate='adaptive', batch_size=64, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32, 16), learning_rate='adaptive', batch_size=64, learning_rate_init=0.001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32, 16), learning_rate='adaptive', batch_size=64, learning_rate_init=0.0001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32, 16), learning_rate='adaptive', batch_size=32, learning_rate_init=0.0001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32, 16), learning_rate='adaptive', batch_size=16, learning_rate_init=0.0001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(512, 128, 32), learning_rate='adaptive', batch_size=128, learning_rate_init=0.0001, max_iter=200, verbose=True) # Score  1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32, 16), learning_rate='adaptive', batch_size=16, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.30791666666666667
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(512, 128, 32), learning_rate='adaptive', batch_size=64, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.0985
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32, 16), learning_rate='adaptive', batch_size=16, learning_rate_init=0.01, max_iter=200, verbose=True) # Score  1.0 Ilgai
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256, 128, 64, 32), learning_rate='adaptive', batch_size=32, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.09908333333333333
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32), learning_rate='adaptive', batch_size=16, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.20216666666666666
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32), learning_rate='adaptive', batch_size=32, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.10325
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32, 16), learning_rate='adaptive', batch_size=16, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.40325
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32, 16), learning_rate='adaptive', batch_size=8, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.10233333333333333
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32, 16), learning_rate='adaptive', batch_size=32, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.0975
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256, 128, 64, 32, 16), learning_rate='adaptive', batch_size=16, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.10233333333333333
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256, 128, 64), learning_rate='adaptive', batch_size=64, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.09908333333333333
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256, 128, 64, 32), learning_rate='adaptive', batch_size=16, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.0975
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(256, 128, 64), learning_rate='adaptive', batch_size=64, learning_rate_init=0.1, max_iter=6, verbose=True) # Score 1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32), learning_rate='adaptive', batch_size=8, learning_rate_init=0.01, max_iter=200, verbose=True) # Score 1.0 daug iterationu
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(128, 64, 32), learning_rate='adaptive', batch_size=8, learning_rate_init=0.01, max_iter=5, verbose=True) # Score 1.0
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(64, 32), learning_rate='adaptive', batch_size=8, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.6969166666666666
#mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(32, 16), learning_rate='adaptive', batch_size=4, learning_rate_init=0.1, max_iter=200, verbose=True) # Score  0.59675
mlp = MLPClassifier(activation="relu", solver='adam', alpha = 0.0005, random_state=123, hidden_layer_sizes=(32, 16), learning_rate='adaptive', batch_size=8, learning_rate_init=0.1, max_iter=200, verbose=True) # Score 1.0




print('Classifier setup')
mlp.fit(X_train, y_train)

print('Training complete')
predictions = mlp.predict(X_test)
score = mlp.score(X_test, y_test)
print("Score ",score)



labels = sorted(list(set(y_test)), reverse = False)

# Berechne Confusion Matrix:
cm = confusion_matrix(y_test, predictions, labels=labels)
#cm = cm[::-1, ::-1], T
#Plotte Confusion-Matrix:
print(cm)
fig=plt.figure("Heatmap - Confusionmatrix")
fig.set_size_inches(w=8, h=6)
ax = fig.add_subplot(111)
cax = ax.matshow(cm)

maxi = np.amax(cm)
mini = np.amin(cm)


#for is_digit_MNIST:
#    labels = sorted(list(set(y_test)), reverse = False)
#else:
#labels = [label_dict[elem] for elem in range(10)]

for i in range(len(labels)):
    for j in range(len(labels)):
        c = cm[j,i]
        if c > 0.75 * maxi:
            ax.text(i, j, str(c), ca='center', ha = 'center')
        else:
            ax.text(i, j, str(c), va='center', ha = 'center', color = (0.99, 0.9, 0.14))

fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.yaxis.set_major_locator(MultipleLocator(1))

plt.xlabel("\nGround Truth")
plt.ylabel("\nPredicted")
plt.show()













