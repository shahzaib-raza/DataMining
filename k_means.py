# Imports
import pandas as pd
import category_encoders as ce
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Converting the data into Pandas DataFrame object
df: pd.DataFrame = pd.DataFrame(pd.read_csv("data.csv"))

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

# Initializing K-Means object with 3 clusters (as our data have 3 clusters)
classifier = KMeans(n_clusters=3)

# Fitting model_year and price data into K-Means classifier as these features are the major ones which classify a car
classifier.fit_predict(df[['model_year', 'price']])

# The labels classified by our K-Means classifier
y_pred = classifier.labels_

# Plotting the data with K-means clusters

# Figure, axes of SubPlot object
f, xs = plt.subplots()
# Scatter plot
sc = xs.scatter(y=df['price'], x=df['model_year'], c=y_pred)
# legends
legends = xs.legend(*sc.legend_elements(), title='clusters')
# Plot title
plt.title("Clustering using K-Means")
# X-axis label
plt.xlabel("model year")
# Y-axis label
plt.ylabel("price")
# Adding legends in figure
xs.add_artist(legends)
# Display plot
plt.show()
