# Imports
import pandas as pd
import category_encoders as ce
from sklearn import model_selection
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# Converting the data into Pandas DataFrame object
df: pd.DataFrame = pd.DataFrame(pd.read_csv("data.csv"))

# Dropping category and price columns as the program have to predict category without observing the price
x: pd.DataFrame = df.drop(['category', 'price'], axis=1)

# Category is what our program to predict
y: pd.Series = df['category']

# Converting our qualitative columns into quantitative columns
x_encoder: ce.OrdinalEncoder = ce.OrdinalEncoder(cols=['make',
                                                       'air_bags',
                                                       'air_conditioning',
                                                       'power_windows',
                                                       'power_steering',
                                                       'sun_roof',
                                                       'alloy_rims'])
x: pd.DataFrame = x_encoder.fit_transform(x)

# Also converting the predictor from qualitative into quantitative
y_encoder = ce.OrdinalEncoder(cols=['category'])
y: pd.Series = y_encoder.fit_transform(y)

# Splitting the data into train and test sets
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)

print(x_train.head())
print("__________________________________________________________________")

# The list of criterion used in DecisionTreeClassifier
criterion: list = ['gini', 'entropy']

# Iterating to observe result of DecisionTreeClassifier for each criteria
for criteria in criterion:
    # Classifier class
    dt: tree.DecisionTreeClassifier = tree.DecisionTreeClassifier(criterion=criteria, max_depth=3)

    # Training the classifier
    dt.fit(x_train, y_train)

    # Predicting the test data
    y_pred: [] = dt.predict(x_test)

    # Observing the accuracy score
    acc: float = accuracy_score(y_test, y_pred)
    print("Accuracy score for " + criteria + " criterion: ", acc)

    # Observing confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion matrix for " + criteria + " criterion: ")
    print(cm)

    print("------------------------------------------------------")

    # Plotting results in pyPlot figure
    fig = plt.figure(figsize=(9, 5))
    tr = tree.plot_tree(dt, filled=True)
    plt.show()
