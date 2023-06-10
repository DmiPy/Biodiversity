import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Read observations and species info data
observations = pd.read_csv("observations.csv")
species = pd.read_csv("species_info.csv")

# Filter species data by dropping rows with missing conservation status
filtered_species = species.dropna(subset=["conservation_status"])

# Merge observations and filtered species data on scientific_name
df = pd.merge(observations, filtered_species, on="scientific_name")

# Select necessary columns for correlation analysis
selected_columns = ['observations', 'category', 'conservation_status']

# Create a new DataFrame with selected columns
selected_data = df[selected_columns]

# Remove rows with missing values
selected_data = selected_data.dropna()

# Convert categorical data to numerical format
selected_data['category'] = selected_data['category'].astype(
    'category').cat.codes
selected_data['conservation_status'] = selected_data['conservation_status'].astype(
    'category').cat.codes

# Create correlation matrix
correlation_matrix = selected_data.corr()

# Create a heatmap of correlations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
plt.close()

# Group data by category and calculate the sum of observations in each category
category_counts = df.dropna(subset=["category"]).groupby("category").sum()

# Create a bar chart for category observations
category_counts.plot(kind='bar', legend=None)
plt.xlabel('Animal Category')
plt.ylabel('Number of Observations')
plt.title('Distribution of Observations by Animal Categories')
plt.xticks(rotation=0)
plt.show()
plt.close()

# Create a strip plot for the correlation between conservation status and observations
plt.figure(figsize=(10, 6))
sns.set()
sns.stripplot(data=df, x="conservation_status",
              y="observations", hue="park_name")
plt.xlabel('Conservation Status')
plt.ylabel('Number of Observations')
plt.title('Correlation between Conservation Status and Observations')
plt.show()
plt.close()

# Group data by scientific name and collect unique common names for each species
species_mapping = df.groupby('scientific_name')['common_names'].unique()

# Find duplicates or different designations
duplicate_species = species_mapping[species_mapping.apply(
    lambda x: len(x) > 1)]

# Display duplicates or different designations
print("Duplicates or different designations for the same species:")
print(duplicate_species)
