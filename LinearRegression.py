from sklearn.model_selection import train_test_split
from sklearn import linear_model
from Task import *

X_train, X_test, y_train, y_test = train_test_split(df['JEE_SCORE'], PERCENT_IN_12TH_CLASS, test_size=0.2)

X_train = (np.array(X_train)).reshape(800, 1)
X_test = (np.array(X_test)).reshape(200, 1)

print X_train.shape, y_train.shape
print X_test.shape, y_test.shape
# print(len(X_train), len(X_test))
# print(len(y_train), len(y_test))

lm = linear_model.LinearRegression()

model = lm.fit(X_train, y_train)
predictions = lm.predict(X_test)

print "Score:", model.score(X_test, y_test)

print(predictions[:10])
plt.plot(y_test, predictions)
plt.xlabel("True Values")
plt.ylabel("Predictions")
plt.show()