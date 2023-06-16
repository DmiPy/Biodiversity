# Biodiversity In National Parks

This project analyzes biodiversity data in national parks using Python and data visualization libraries such as pandas, matplotlib, numpy, and seaborn.

## Description

The code in this project performs the following tasks:

1. Reads the observations and species info data from CSV files.
2. Filters the species data by dropping rows with missing conservation status.
3. Merges the observations and filtered species data based on scientific name.
4. Selects the necessary columns for correlation analysis.
5. Creates a new DataFrame with the selected columns.
6. Removes rows with missing values.
7. Converts categorical data to numerical format.
8. Creates a correlation matrix of the selected data.
9. Generates a heatmap of the correlation matrix.
10. Groups the data by category and calculates the sum of observations in each category.
11. Creates a bar chart to visualize the distribution of observations by animal categories.
12. Creates a strip plot to explore the correlation between conservation status and observations.
13. Identifies duplicates or different designations for the same species based on scientific name.

## Dependencies

The code requires the following Python libraries to be installed:

- pandas
- matplotlib
- numpy
- seaborn

## Usage

1. Clone the repository or download the project files.
2. Place the observations.csv and species_info.csv files in the same directory as the Python script.
3. Run the Python script using a compatible Python interpreter.
4. The output will include visualizations of the correlation matrix, distribution of observations by animal categories, and the correlation between conservation status and observations.
5. The script will also print any duplicates or different designations found for the same species.

## Data Sources

- observations.csv: Contains observation data for different species.
- species_info.csv: Contains information about various species, including scientific names, common names, and conservation status.

## Results

The project provides insights into the biodiversity in national parks by analyzing the correlation between different factors and visualizing the distribution of observations. The generated visualizations help understand the relationships between the conservation status of species, their categories, and the number of observations.

## Future Improvements

- Explore additional statistical analysis techniques to gain more insights.
- Enhance the visualization by adding more interactive features.
- Incorporate machine learning algorithms for predictive analysis.
