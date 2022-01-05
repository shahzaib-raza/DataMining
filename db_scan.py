# Imports
import pandas as pd
import category_encoders as ce
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Converting the data into Pandas DataFrame object
df = pd.DataFrame(pd.read_csv("data.csv"))

# Observing the data set
print(df.head())
print("__________________________________________________________________")

# Category is what our program to predict
y: pd.Series = df['category']

# Converting non numeric values into numeric by encoding them
y_encoder = ce.OrdinalEncoder(cols=['category'])
y_encode = y_encoder.fit_transform(df['category'])

# Creating a list of encoded values of 'Y' so that we can provide color according to clusters in the data
colors = pd.Series(y_encode['category']).tolist()

# Plotting the data with clustering by humans

# Figure and Axes of SubPlot object
fig, ax = plt.subplots()
# Scatter plot
scat = ax.scatter(x=df['model_year'], y=df["price"], c=colors)
# Legends
leg = ax.legend(*scat.legend_elements(), title='clusters')
# Plot title
plt.title("Clusters on basis of classification by human")
# X-axis label
plt.xlabel("model_year")
# Y-axis label
plt.ylabel("price")
# Adding legends in figure
ax.add_artist(leg)
# Display plot
plt.show()

"""
* It is necessary to normalize all data in the dataset before training the DBSCAN model over it.
* Because DBSCAN is purely based on distance and if the values are highly differ from each other it will marks all
  points as outliers.
"""

# Initializing a StandardScaler class as it will preprocess our columns
sc = preprocessing.StandardScaler()

# Processed data
processed = pd.DataFrame(sc.fit_transform(df[['model_year', 'price']]), columns=['model_year', 'price'])

# Observing processed data
print(processed.head())
print("__________________________________________________________________")

# Initializing DBSCAN object with number of min points near center as 3 and max distance b/w two neighbours as 0.5
classifier = DBSCAN(eps=0.5, min_samples=3)

# Fitting processed data into DBSCAN model
y_pred = classifier.fit_predict(processed)

# Plotting the data with K-means clusters

# Figure, axes of SubPlot object
f, xs = plt.subplots()
# Scatter plot
sc = xs.scatter(y=df['price'], x=df['model_year'], c=y_pred)
"""
Note:
    DBSCAN algorithm mark outliers with label "-1". So you will see outliers of data marked with legend of "-1" color
in the plot.
"""
# legends
legends = xs.legend(*sc.legend_elements(), title='clusters')
# Plot title
plt.title("Clustering using DBSCAN")
# X-axis label
plt.xlabel("model year")
# Y-axis label
plt.ylabel("price")
# Adding legends in figure
xs.add_artist(legends)
# Display plot
plt.show()
