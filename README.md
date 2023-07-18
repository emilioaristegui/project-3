# Project-3
CO2 Emissions Around the World

## Background
Our project aims to investigate the primary contributors to global pollution by analyzing various countries, industries, and segments. We will identify the countries with the highest pollution rates, determining the types that cause the most pollution, and discover the specific segments responsible for significant pollution levels. 

- Which countries pollute the most?
  
- Which type causes the most pollution? 
    
- Which segment causes the most pollution? 

## Contents
- /API/dev/project_3.ipynb.
- /API/static/groupby.json.
- /API/static/logic.js.
- /API/static/merged.json.
- /API/static/style.css
- /data/Data.sql.
- /data/Methane_final.csv.
- /data/average-latitude-longitude-countries.csv.
- /data/merged_df.csv
- .DS_store
- README.md: This file, providing an overview of the project and instructions for usage.

## Initial Requirements
Tell a story using data visualizations. Here are the specific requirements:
- Your visualization must include a Python Flask-powered API, HTML/CSS, JavaScript, and at least one database (SQL, MongoDB, SQLite, etc.).

Your project should fall into one of the following three tracks:
- A combination of web scraping and Leaflet or Plotly
- SELECTED: A dashboard page with multiple charts that update from the same data
- A server that performs multiple manipulations on data in a database prior to visualization (must be approved)

- Your project should include at least one JS library that we did not cover.
- Your project must be powered by a dataset with at least 100 records.
- Your project must include some level of user-driven interaction (e.g., menus, dropdowns, textboxes).
- Your final visualization should ideally include at least three views.

Focus your efforts within a specific industry:
- SELECTED: Energy

## Guidelines:

1. Check for copyright protections, and make sure that the way you plan to use this dataset is within the bounds of fair use. 
- Data is from kaggle and it provides the source: International Energy Agency
2. Document how you intend to use this dataset now and in the future. Find any licenses or terms of use associated with the dataset, and review them to confirm that your intended use is in compliance.
- License: Attribution 4.0 International (CC BY 4.0)
- The objective of the project is to show how countries contribute to global pollution.
3. Investigate how the dataset was collected. Identify any indicators that the data was obtained from a source that the compilers were not authorized to access.
- Consists of merging list with coordinates with kaggle csv to clean the data and add more information to create the visualization, merge with perimeter of country for graph.
- The source was authorized by the presented license.

## Data Cleanup and Analysis
- Jupyter Notebook
- The analysis process can be broken into two broad phases:
    - (1) exploration and cleanup.
    - (2) analysis.
- Aggregation, correlation, comparison, summary statistics, sentiment analysis, and time-series analysis.
- Plots during both the exploration and analysis phases.

## Technical Requirements

### Data and Delivery

- Data components used in the project are clearly documented. 
- The dataset contains at least 100 unique records.
- A database is used to house the data (SQL, MongoDB, SQLite, etc.). 
- The project is powered by a Python Flask API and includes HTML/CSS, JavaScript, and the chosen database. 

### Back End

- The page created to showcase data visualizations runs without error. 
- A JavaScript library not shown in class is used in the project. 
- The project conforms to one of the following designs:
    - A Leaflet or Plotly chart built from data gathered through web scraping
    - A dashboard page with multiple charts that all reference the same data

### Visualizations

- A minimum of three unique views present the data. 
- Multiple user-driven interactions (such as dropdowns, filters, or a zoom feature) are included on the final page.
- The final page displays visualizations in a clear, digestible manner. 
- The data story is easy to interpret for users of all levels. 

### Group Presentation

- All group members speak during the presentation. 
- The content is relevant to the project. 
- The presentation maintains audience interest. 
- Content, transitions, and conclusions flow smoothly within any time restrictions.

## Contributions
If you would like to contribute to this project, you can follow these steps:

Fork the repository.
Create a new branch for your changes.
Make your modifications and enhancements.
Test your changes thoroughly.
Submit a pull request, explaining the purpose and benefits of your modifications.
Please ensure that your contributions align with the goals of the project and adhere to the coding standards and best practices.

## Contact
If you have any questions, suggestions, or feedback, please feel free to contact us!

Thank you for your interest in this project!
