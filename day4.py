# -*- coding: utf-8 -*-
"""Day4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wYdLJIx8XFN9YT-iOyrLEO8DWmlgdX5G
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
    roc_curve,
    classification_report
)

# Step 1: Load the dataset
url = "/content/data (1).csv"  # Replace with actual if needed
data = pd.read_csv("/content/data (1).csv")  # backup URL

# Drop unnamed column if present
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Preview
print("Dataset shape:", data.shape)
data.head()

# Step 2: Data Preprocessing
# Drop ID column if present
if 'id' in data.columns:
    data.drop('id', axis=1, inplace=True)

# Convert diagnosis column to binary (M = 1, B = 0)
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

# Split into features and target
X = data.drop('diagnosis', axis=1)
y = data['diagnosis']

# Step 3: Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 6: Evaluate the Model
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Precision, Recall, ROC-AUC
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_prob)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"ROC AUC Score: {roc_auc:.4f}")

# ROC Curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
plt.plot(fpr, tpr, label=f'ROC Curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid(True)
plt.show()

# Step 7: Threshold tuning
threshold = 0.3  # change as needed
y_custom_pred = (y_prob > threshold).astype(int)
print(f"New Confusion Matrix @ threshold = {threshold}")
print(confusion_matrix(y_test, y_custom_pred))

# Step 8: Sigmoid Function Explanation (Optional visualization)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z_vals = np.linspace(-10, 10, 100)
sig_vals = sigmoid(z_vals)

plt.plot(z_vals, sig_vals)
plt.title("Sigmoid Function")
plt.xlabel("z")
plt.ylabel("Sigmoid(z)")
plt.grid(True)
plt.show()