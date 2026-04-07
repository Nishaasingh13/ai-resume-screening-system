import pandas as pd

# Load dataset
data = pd.read_csv("dataset.csv")

print("Columns:", data.columns)

# Rename columns
data.columns = ["category", "resume_text"]

# Remove null values
data.dropna(inplace=True)

# Convert to lowercase
data["resume_text"] = data["resume_text"].astype(str).str.lower()

# Remove duplicates
data.drop_duplicates(inplace=True)

# Save cleaned dataset
data.to_csv("cleaned_dataset.csv", index=False)

print("✅ Dataset cleaned successfully!")
print(data.head())