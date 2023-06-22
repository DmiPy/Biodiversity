# Biodiversity In National Parks

This project analyzes biodiversity data in national parks using Python and data visualization libraries such as pandas, matplotlib, numpy, and seaborn.

## Description

The code in this project performs the following tasks:

1. ### Removes rows and missing values or duplicates
2. ### Adjusts the data to the required format
3. ### Creates a correlation matrix of the selected data.
4. ### Generates a heatmap of the correlation matrix.

![category_conservation_heatmap](https://github.com/DmiPy/Biodiversity/assets/128055633/836fb916-edb2-42d0-87d1-312d08b54d75)

5. ### Creates a bar chart to visualize the distribution of observations by animal categories.

![animal_observations_bar](https://github.com/DmiPy/Biodiversity/assets/128055633/ba5ff335-e409-4b6b-8268-12dc1818c6e4)

7. ### Creates a strip plot to explore the correlation between conservation status and observations.

![conservation_observations_strip](https://github.com/DmiPy/Biodiversity/assets/128055633/deddcad1-50fb-4af7-b501-b864e38831f6)

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
