# Data Cleaning - Check for missing values and data issues
print("Data Cleaning Analysis:")
print("=" * 50)
print("Missing values in each column:")
print(df.isnull().sum())

# Check for zero values that might indicate missing data
print("\nZero values in each column (potential missing data):")
zero_counts = (df == 0).sum()
print(zero_counts)

# Identify columns that shouldn't have zero values biologically
problematic_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
print("\nProblematic zero values (should not be zero biologically):")
for col in problematic_zeros:
    zero_count = (df[col] == 0).sum()
    zero_percentage = (zero_count / len(df)) * 100
    print(f"{col}: {zero_count} zeros ({zero_percentage:.2f}%)")

# Replace zeros with NaN for problematic columns (except Insulin where 0 might be valid)
df_cleaned = df.copy()
for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']:
    df_cleaned[col] = df_cleaned[col].replace(0, np.nan)

print("\nAfter replacing zeros with NaN:")
print(df_cleaned.isnull().sum())

# Replace missing values with median (more robust for outliers)
for col in ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI']:
    median_value = df_cleaned[col].median()
    df_cleaned[col] = df_cleaned[col].fillna(median_value)
    print(f"Filled {col} missing values with median: {median_value}")

print("\nFinal missing values check:")
print(df_cleaned.isnull().sum())