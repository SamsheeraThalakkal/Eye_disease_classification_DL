import pandas as pd

# Load CSV
df = pd.read_csv("full_df.csv")

# Disease columns
disease_cols = ['N', 'D', 'G', 'C', 'A', 'H', 'M', 'O']

# Count number of diseases per patient
df['disease_count'] = df[disease_cols].sum(axis=1)

# Multi-disease patients (more than 1 disease)
multi_disease_df = df[df['disease_count'] > 1]

print("Total Patients:", len(df))
print("Multi-Disease Patients:", len(multi_disease_df))

# If you want their image IDs
print("\nPatient IDs with Multiple Diseases:")
print(multi_disease_df['ID'].tolist())