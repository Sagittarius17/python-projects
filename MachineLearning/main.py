from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Load the digits dataset
digits = load_digits()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=45)

# Train a neural network classifier
clf = MLPClassifier(hidden_layer_sizes=(64,), max_iter=1000)
clf.fit(X_train, y_train)

# Predict the digits for the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
