import pandas as pd
import os

print("Current Directory:", os.getcwd())

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Show initial preview
print(df.head())

# Check and handle missing values
df['rating'].fillna('Not Rated', inplace=True)
df['country'].fillna('unknown', inplace=True)
df.dropna(subset=['director'], inplace=True)

# Remove duplicates
df = df.drop_duplicates()

# Standardize text
df['country'] = df['country'].str.strip().str.lower()

# Convert dates
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

# Save cleaned file
df.to_csv('netflix_cleaned.csv', index=False)

print("✅ Data cleaned and saved successfully as 'netflix_cleaned.csv'")
