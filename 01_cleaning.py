import pandas as pd

# 1. Load the data
print("Loading data...")
df = pd.read_csv('../data/churn.csv')

print("Data loaded successfully!")

# 2. Look at the first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# 3. Fix missing values in TotalCharges
# 'coerce' turns any bad text into NaN (Not a Number), then we fill it with 0
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# 4. Create a new column for tenure in years
df['tenure_years'] = (df['tenure'] / 12).round(1)

# 5. Save the clean data
df.to_csv('../data/cleaned_churn.csv', index=False)
print("\nCleaning complete! Saved to data/cleaned_churn.csv")