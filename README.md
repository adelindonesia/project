# Airline Ticket Price Prediction

The goal of this project was to develop a model that could accurately predict the prices of round-trip airline tickets from Lufthansa and Swiss airlines to São Paulo and New York City. By determining the optimal time to purchase tickets for each destination, we aimed to achieve significant savings and maximize the travel budget.

To accomplish this, we analyzed historical data on ticket prices and other relevant factors to identify patterns and trends that could be used to forecast future ticket prices. Our analysis revealed several key variables that influenced ticket prices, including the time at which flight ticket data is collected and airline-specific factors.

Our predictive model, trained on historical data using linear regression, was found to have a reasonable level of predictive accuracy. This project provided valuable experience in working with time series data and developing predictive models while also uncovering practical ways to save money on air travel.

## Project Folder Structure

This repository contains several sub-folders, including:

- `report_project`: This folder contains the project report in the form of a PDF file, `report.pdf`, which is generated from the `report.tex` file.

- `second_version`: This folder contains all relevant code for the project, representing the final version. It includes three sub-folders:
  - `webscraping`: This folder contains the `web_scraping.ipynb` file, which is the code used to scrape data for the project. It also includes two sub-folders, one for each destination (São Paulo and New York City), which contain the data collected in CSV and XLSX formats.
  - `data_cleaning`: This folder contains several files essential for the data visualization part of the project, including `data_cleaning.ipynb`, `data_visualization.ipynb`, and `data_exploration.ipynb`.
  - `data_model`: This folder contains the `data_model.ipynb` file, which is the code used to conduct the modeling part of the project.

- `test`: This folder contains trial and error versions of the code that are not essential for understanding the project but have been included to provide a historical record of its development.
