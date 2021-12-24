import pandas as pd
import category_encoders as ce
from sklearn import model_selection
from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

df = pd.DataFrame(pd.read_csv("data.csv"))
x = df.drop(['category'], axis=1)
y = df['category']
x_encoder = ce.OrdinalEncoder(cols=['make',
                                    'air_bags',
                                    'air_conditioning',
                                    'power_windows',
                                    'power_steering',
                                    'sun_roof',
                                    'alloy_rims'])
x = x_encoder.fit_transform(x)
y_encoder = ce.OrdinalEncoder(cols=['category'])
y = y_encoder.fit_transform(y)
x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y)
print(x_train.head())
print("__________________________________________________________________")
criterion = ['gini', 'entropy']
for criteria in criterion:
    dt_gini = tree.DecisionTreeClassifier(criterion=criteria, max_depth=3)
    dt_gini.fit(x_train, y_train)
    y_pred = dt_gini.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    print("Accuracy score for " + criteria + " criterion: ", acc)
    print("Confusion matrix for " + criteria + " criterion: ")
    print(cm)
    print("------------------------------------------------------")
    fig = plt.figure(figsize=(9, 5))
    tr = tree.plot_tree(dt_gini, filled=True)
    plt.show()
