import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

# Load the diabetes dataset
df = pd.read_csv('diabetes.csv')

# Display basic info about the dataset
print("Dataset shape:", df.shape)
print("Column names:", df.columns.tolist())
print("Data types:")
print(df.dtypes)

# Select only numerical columns for correlation
numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print("Numerical columns:", numerical_cols)

# Calculate correlation matrix
correlation_matrix = df[numerical_cols].corr()
print("Correlation matrix shape:", correlation_matrix.shape)

# Create the heatmap
fig = go.Figure(data=go.Heatmap(
    z=correlation_matrix.values,
    x=correlation_matrix.columns,
    y=correlation_matrix.columns,
    colorscale='RdBu',  # Diverging colormap (red-blue)
    zmin=-1,
    zmax=1,
    text=np.round(correlation_matrix.values, 2),  # Show correlation values
    texttemplate='%{text}',
    textfont={'size': 10},
    showscale=True,
    colorbar=dict(title='Correlation')
))

# Update layout
fig.update_layout(
    title='Diabetes Dataset Corr Matrix',
    xaxis_title='Variables',
    yaxis_title='Variables'
)

# Make sure the plot is square and readable
fig.update_xaxes(side='bottom')
fig.update_yaxes(autorange='reversed')

# Save the chart as both PNG and SVG
fig.write_image('correlation_heatmap.png')
fig.write_image('correlation_heatmap.svg', format='svg')

print("Chart saved successfully!")