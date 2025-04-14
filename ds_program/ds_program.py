import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns

# Load the dataset
df = pd.read_csv('Credit_Card_Applications.csv')

# Display the first few rows
print(df.head())

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed.columns)

# Separate features and target variable
X = df_imputed.drop('Class', axis=1)  # 'Approved' is the target variable
y = df_imputed['Class']

# Standardize the features
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=200)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Initialize the K-Means model
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit the model
df_imputed['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(x='A1', y='A2', hue='Cluster', data=df_imputed, palette='Set1')
plt.title('K-Means Clusters')
plt.xlabel('Feature1')
plt.ylabel('Feature2')
plt.savefig("KMeans_Cluster.png")
