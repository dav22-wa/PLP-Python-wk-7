import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Set seaborn style for better visualization
sns.set_style("whitegrid")

def load_data():
    """Load Iris dataset with error handling"""
    try:
        # Load iris dataset from sklearn
        iris = load_iris()
        df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

def explore_data(df):
    """Explore dataset structure and handle missing values"""
    print("\nDataset Exploration:")
    print("--------------------")
    
    # Display first few rows
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    # Display data types and basic info
    print("\nDataset Info:")
    print(df.info())
    
    # Check for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # If missing values exist, fill with mean for numerical columns
    if df.isnull().any().any():
        print("\nHandling missing values...")
        numerical_cols = df.select_dtypes(include=['float64']).columns
        df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())
        print("Missing values filled with column means")

def analyze_data(df):
    """Perform basic statistical analysis"""
    print("\nBasic Statistical Analysis:")
    print("--------------------------")
    
    # Basic statistics
    print("\nStatistical Summary:")
    print(df.describe())
    
    # Group by species and calculate means
    print("\nMean measurements by species:")
    group_means = df.groupby('species').mean()
    print(group_means)
    
    return group_means

def create_visualizations(df, group_means):
    """Create four different types of visualizations"""
    
    # 1. Line chart: Mean measurements across species
    plt.figure(figsize=(10, 6))
    for column in group_means.columns:
        plt.plot(group_means.index, group_means[column], marker='o', label=column)
    plt.title('Mean Measurements by Iris Species')
    plt.xlabel('Species')
    plt.ylabel('Measurement (cm)')
    plt.legend()
    plt.savefig('line_chart.png')
    plt.close()
    
    # 2. Bar chart: Average sepal length by species
    plt.figure(figsize=(8, 6))
    sns.barplot(x=group_means.index, y=group_means['sepal length (cm)'])
    plt.title('Average Sepal Length by Species')
    plt.xlabel('Species')
    plt.ylabel('Sepal Length (cm)')
    plt.savefig('bar_chart.png')
    plt.close()
    
    # 3. Histogram: Sepal length distribution
    plt.figure(figsize=(8, 6))
    sns.histplot(data=df, x='sepal length (cm)', bins=20)
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Count')
    plt.savefig('histogram.png')
    plt.close()
    
    # 4. Scatter plot: Sepal length vs Petal length
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                   hue='species', size='species')
    plt.title('Sepal Length vs Petal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.savefig('scatter_plot.png')
    plt.close()

def main():
    # Load data
    df = load_data()
    if df is None:
        return
    
    # Explore data
    explore_data(df)
    
    # Analyze data
    group_means = analyze_data(df)
    
    # Create visualizations
    create_visualizations(df, group_means)
    
    # Print findings
    print("\nKey Findings:")
    print("-------------")
    print("1. Setosa species has the smallest measurements across all features")
    print("2. Virginica species generally has the largest measurements")
    print("3. Sepal length and petal length show a positive correlation")
    print("4. Clear separation between species in scatter plot of sepal vs petal length")

if __name__ == "__main__":
    main()