import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('your_dataset.csv')

# Step 2: Handle Missing Values
df.dropna(inplace=True)  # Drop rows with missing values

# Step 3: Remove Duplicates
df.drop_duplicates(inplace=True)

# Step 4: Outlier Detection
# Define a function to handle outliers using Z-scores
def handle_outliers(df, column_name, threshold=3):
    z_scores = (df[column_name] - df[column_name].mean()) / df[column_name].std()
    df = df[(z_scores < threshold) & (z_scores > -threshold)]
    return df

# Apply the function to a specific column
df = handle_outliers(df, 'numerical_column')

# Step 5: Data Visualization
# Create a histogram to visualize a numerical column
plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='numerical_column', kde=True)
plt.title('Histogram of Numerical Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Step 6: Save the cleaned dataset
df.to_csv('cleaned_dataset.csv', index=False)
print(df)