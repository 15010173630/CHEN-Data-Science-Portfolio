from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

st.title("Bank Marketing ML Lab")

# Step 1: Load and inspect the data.
csv_path = Path(__file__).parent / "data" / "bank_marketing.csv"
data = pd.read_csv(csv_path)

st.subheader("1. Load and inspect the data")
st.markdown("[OpenML Bank Marketing sample](https://www.openml.org/search?id=1461&type=data)")
st.write(f"The sample contains {len(data):,} rows.")
st.dataframe(data.head())

# Step 2: Choose the target (y) and the input features (X).
st.subheader("2. Choose a target")
target = st.selectbox("Target column", ["subscribed", "housing", "loan", "default"])
y = data[target]

# These numeric features are available before the call.
feature_columns = ["age", "balance", "pdays", "previous"]
X = data[feature_columns]
st.write("Features used: age, balance, days since the previous campaign, and prior contacts.")

# Step 3: Split the data into training and test sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train the decision tree.
st.subheader("3. Train a decision tree")
max_depth = st.slider("Maximum depth", 1, 20, 4)
min_samples_leaf = st.slider("Minimum samples per leaf", 1, 100, 20)
st.caption("Depth limits how far the tree can split. Leaf size sets the minimum number of rows in each final group.")

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=max_depth,
    min_samples_leaf=min_samples_leaf,
)
model.fit(X_train, y_train)

# Step 5: Predict and evaluate on the test set.
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, pos_label="yes")

st.subheader("4. Evaluate on the test set")
st.write(f"Training rows: {len(X_train):,} | Test rows: {len(X_test):,}")
st.metric("Accuracy", f"{accuracy:.1%}")
st.caption("The share of all test rows that the model classified correctly.")
st.metric("Recall for yes", f"{recall:.1%}")
st.caption("Of the test rows actually labeled yes, the share the model correctly found.")

cm = confusion_matrix(y_test, y_pred, labels=["no", "yes"])
fig, ax = plt.subplots()
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=["no", "yes"], yticklabels=["no", "yes"], ax=ax,
)
ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
st.pyplot(fig)
plt.close(fig)
