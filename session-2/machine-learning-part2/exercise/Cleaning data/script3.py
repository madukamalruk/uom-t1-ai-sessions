# Outlier Detection and Removal using IQR method
print("Outlier Detection and Removal:")
print("=" * 50)

# Function to detect outliers using IQR
def detect_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound

# Check for outliers in each numerical column
numerical_cols = df_cleaned.select_dtypes(include=[np.number]).columns.drop('Outcome')
outlier_info = {}

print("Outlier analysis for each column:")
for col in numerical_cols:
    outliers, lower, upper = detect_outliers_iqr(df_cleaned, col)
    outlier_count = len(outliers)
    outlier_percentage = (outlier_count / len(df_cleaned)) * 100
    outlier_info[col] = {
        'count': outlier_count,
        'percentage': outlier_percentage,
        'lower_bound': lower,
        'upper_bound': upper
    }
    print(f"{col}: {outlier_count} outliers ({outlier_percentage:.2f}%), Range: [{lower:.2f}, {upper:.2f}]")

# Remove outliers (keeping moderate approach - only remove extreme outliers)
df_no_outliers = df_cleaned.copy()
initial_size = len(df_no_outliers)

# Remove outliers for selected columns with high outlier counts
cols_to_clean = ['Insulin', 'BMI', 'DiabetesPedigreeFunction']
for col in cols_to_clean:
    if outlier_info[col]['count'] > 0:
        Q1 = df_no_outliers[col].quantile(0.25)
        Q3 = df_no_outliers[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_no_outliers = df_no_outliers[(df_no_outliers[col] >= lower_bound) & 
                                       (df_no_outliers[col] <= upper_bound)]

final_size = len(df_no_outliers)
removed_rows = initial_size - final_size
print(f"\nRows removed due to outliers: {removed_rows} ({(removed_rows/initial_size)*100:.2f}%)")
print(f"Final dataset size: {final_size}")

# Save cleaned data
df_no_outliers.to_csv('diabetes_cleaned.csv', index=False)
print("\nCleaned data saved as 'diabetes_cleaned.csv'")