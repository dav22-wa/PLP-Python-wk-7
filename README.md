Iris Dataset Analysis
Overview
This project analyzes the Iris dataset using Python, pandas, and matplotlib. It includes data loading, exploration, basic statistical analysis, and four different visualizations to understand the characteristics of Iris flowers across different species.
Requirements
To run the analysis, you need the following Python libraries:

pandas
matplotlib
seaborn
scikit-learn
numpy

You can install these dependencies using pip:
pip install pandas matplotlib seaborn scikit-learn numpy

Files

iris_analysis.py: The main Python script containing the complete analysis pipeline.
Output files (generated after running the script):
line_chart.png: Line chart of mean measurements by species
bar_chart.png: Bar chart of average sepal length by species
histogram.png: Histogram of sepal length distribution
scatter_plot.png: Scatter plot of sepal length vs petal length



Usage

Ensure all required libraries are installed.
Run the Python script:

python iris_analysis.py


The script will:
Load the Iris dataset
Display dataset information and statistics
Generate four visualizations saved as PNG files
Print key findings



Analysis Details
Task 1: Data Loading and Exploration

Loads the Iris dataset using scikit-learn
Displays first 5 rows and dataset information
Checks for missing values (handles them if present)
Shows data types and basic structure

Task 2: Basic Data Analysis

Computes statistical summary (mean, median, std, etc.) for numerical columns
Groups data by species and calculates mean measurements
Identifies key patterns in the data

Task 3: Data Visualization
Creates four visualizations, saved as PNG files in the project directory:

Line Chart: Shows mean measurements across species

File: line_chart.png



Bar Chart: Displays average sepal length by species

File: bar_chart.png



Histogram: Shows distribution of sepal length

File: histogram.png



Scatter Plot: Visualizes sepal length vs petal length

File: scatter_plot.png




Note: To view the screenshots, run the script to generate the PNG files, then open them from the project directory or include them in this README when rendering in a Markdown viewer that supports image embedding.
Key Findings

Setosa species has the smallest measurements
Virginica species has the largest measurements
Positive correlation between sepal length and petal length
Clear species separation in scatter plot

Notes

The script includes error handling for data loading
Visualizations are styled using seaborn for better aesthetics
All plots are saved as PNG files with appropriate titles and labels
The Iris dataset is sourced from scikit-learn's built-in datasets

For any issues or questions, please review the script comments or contact the author.
