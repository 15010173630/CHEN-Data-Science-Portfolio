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
st.subheader("1. Load and inspect the data")
uploaded_file = st.file_uploader(
    "Upload a CSV ", type="csv"
)

if not uploaded_file:
    csv_path = Path(__file__).parent / "data" / "bank_marketing.csv"
    data = pd.read_csv(csv_path)
    st.markdown("[OpenML Bank Marketing sample](https://www.openml.org/search?id=1461&type=data)")
else:
    try:
        data = pd.read_csv(uploaded_file)
    except (ValueError, UnicodeError):
        st.error("Could not read the file.")
        st.stop()


st.write(f"The dataset contains {len(data):,} rows.")
st.dataframe(data.head())

# Step 2: Choose the target (y) and the input features (X).
st.subheader("2. Choose a target")
if not uploaded_file:
    target = st.selectbox("Target column", ["subscribed", "housing", "loan", "default"])
    feature_columns = ["age", "balance", "pdays", "previous"]
    st.write("Features used: age, balance, days since the previous campaign, and prior contacts.")
else:
    target = st.selectbox("Target column", data.columns, index=None)
    if target is None:
        st.info("Choose a target column to continue.")
        st.stop()

    feature_options = data.drop(columns=target).columns.tolist()
    feature_columns = st.multiselect("Feature columns", feature_options, default=feature_options)
    if not feature_columns:
        st.warning("Choose at least one feature")
        st.stop()

# Use complete rows from the selected columns.
selected_data = data[feature_columns + [target]]
selected_data = selected_data.replace([float("inf"), float("-inf")], float("nan")).dropna()
dropped_rows = len(data) - len(selected_data)
if dropped_rows:
    st.caption(f"Skipped {dropped_rows:,} rows with missing or infinite values in the selected columns.")

X = selected_data[feature_columns]
y = selected_data[target].astype(str)
labels = sorted(y.unique())
if not 2 <= len(labels) <= 10:
    st.warning("Choose a classification target with 2 to 10 distinct labels among the usable rows.")
    st.stop()

# Step 3: Split the data into training and test sets.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Encode text columns, use the same feature columns in both sets.
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
X_test = X_test.reindex(columns=X_train.columns, fill_value=0)

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

st.subheader("4. Evaluate on the test set")
st.write(f"Training rows: {len(X_train):,} | Test rows: {len(X_test):,}")
st.metric("Accuracy", f"{accuracy:.1%}")
st.caption("The share of all test rows that the model classified correctly.")
recall_eclass = recall_score(y_test, y_pred, labels=labels, average=None)
st.subheader("Recall by class")
st.caption("For each class, recall is the share of its actual test rows that the model correctly identified.")
for label, recall in zip(labels, recall_eclass):
    st.metric(f"Recall for {label}", f"{recall:.1%}")

cm = confusion_matrix(y_test, y_pred, labels=labels)
fig, ax = plt.subplots()
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues",
    xticklabels=labels, yticklabels=labels
)
ax.set_title("Confusion Matrix")
ax.set_xlabel("Predicted")
ax.set_ylabel("Actual")
st.pyplot(fig)
plt.close(fig)
