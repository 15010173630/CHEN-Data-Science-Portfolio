# Bank Marketing ML Lab


[Open the app](https://chen-data-science-portfolio-jdkjhvsweo26n6ykrpu3zk.streamlit.app/)


## Overview

I built this app around a single decision tree. First I used the bank CSV. Once that worked, I added a box for uploading another file. You can change the depth and the minimum number of rows in a leaf and see the tree's new predictions below.

First, try the 45,211 Bank Marketing examples from OpenML by leaving the upload box empty. Here I've chosen four columns from the dataset: age, balance, pdays, previous. The default tree predicts subscribed, meaning did the customer sign up for a term deposit? You can also have the tree predict housing, loan or default instead. For uploaded files you can choose the inputs to the tree too.

The default tree is missing 991 of the 1,058 subscribers in the test data. It is easier for me to understand the number of subscribers it found than accuracy alone. Overall test accuracy is 88.5%. Yes recall is 6.3%, because the tree found 67 subscribers. Both recall scores are above the confusion matrix so you can see which group is being missed as you vary the sliders.

## Try the app

1. Open the app and try the bank sample, or upload a CSV.
2. Pick a target. If you uploaded a file, pick the input columns too.
3. Move either slider and wait for the new results.
4. Read accuracy, recall by class and the confusion matrix.

## Data preparation and evaluation

| Step | What the code does |
| --- | --- |
| Selected rows | Keeps only the chosen features and target |
| Missing values | Drops selected rows containing missing values or infinity and reports the count |
| Upload target | Accepts 2–10 classes after cleaning, with enough examples per class to split |
| Train/test split | 80% training, 20% testing |
| Text features | Uses pandas.get_dummies, then reindex to match test columns to training columns |

| Output | How to read it |
| --- | --- |
| Accuracy | Correct test predictions divided by all test predictions |
| Recall for each class | Correct predictions for that class divided by all actual test rows in that class |
| Confusion matrix | Actual labels down the left, predictions along the bottom, correct answers on the diagonal |

## Model and controls


| Slider | Python parameter | Range | Default | Effect |
| --- | --- | --- | --- | --- |
| Maximum depth | max_depth | 1–20 | 4 | Limits the number of levels in the tree |
| Minimum samples per leaf | min_samples_leaf | 1–100 | 20 | Sets the minimum training rows in each final group |


## Run locally


Use Python 3.11, the version used for local testing.


1. Clone the repository and enter it.


```bash
git clone https://github.com/15010173630/CHEN-Data-Science-Portfolio.git
cd CHEN-Data-Science-Portfolio
```


2. Create and activate a virtual environment.


```bash
python3 -m venv .venv
source .venv/bin/activate
```


On Windows, activate it with `.venv\Scripts\activate` instead.


3. Install the dependencies.


```bash
python -m pip install -r MLStreamlitApp/requirements.txt
```


4. Start the app.


```bash
python -m streamlit run MLStreamlitApp/app.py
```


5. Open the local URL printed in the terminal. Keep the data folder next to app.py.


## Libraries


| Library | Version | Used for |
| --- | --- | --- |
| Streamlit | 1.52.2 | Page, upload, controls, and results |
| pandas | 2.3.3 | CSV reading and data preparation |
| scikit-learn | 1.7.2 | Splitting, decision tree, and metrics |
| Matplotlib | 3.10.8 | Figure and axes |
| Seaborn | 0.13.2 | Confusion matrix heatmap |



## References


- [Streamlit file uploader documentation](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader)
- [scikit-learn DecisionTreeClassifier documentation](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [pandas get_dummies documentation](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
- [OpenML Bank Marketing dataset #1461](https://www.openml.org/search?id=1461&type=data)

