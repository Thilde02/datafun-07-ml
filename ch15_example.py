import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score

# Load the digits dataset
digits = datasets.load_digits()

# Visualize the first image in the dataset
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)
plt.show()

# Print the corresponding label of the first image
print(f"Label of first image: {digits.target[0]}")

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3, random_state=42)

# Initialize k-NN classifier with 3 neighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Predict on the test data
y_pred = knn.predict(X_test)

# Evaluate the model
print("Classification report:\n", classification_report(y_test, y_pred))
print(f"Accuracy score: {accuracy_score(y_test, y_pred)}")

# Plot the first few test images and their predictions
plt.figure(figsize=(10, 3))

for index, (image, label) in enumerate(zip(X_test[:5], y_pred[:5])):
    plt.subplot(1, 5, index + 1)
    plt.imshow(image.reshape(8, 8), cmap=plt.cm.gray_r)
    plt.title(f"Pred: {label}")
    plt.axis('off')

plt.show()
