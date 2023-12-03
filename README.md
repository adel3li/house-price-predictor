# House Sales Project

## Description

This repository contains the code and data for a project related to house sales. The project involves data cleaning, exploratory data analysis (EDA), profiling, and model training and validation. The project is structured with specific folders for data, code, and various outputs.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Code](#code)
6. [Exploratory Data Analysis](#exploratory-data-analysis)
7. [Data Cleaning](#data-cleaning)
8. [Model Training](#model-training)
9. [Validation](#validation)
10. [Streamlit App](#streamlit-app)
11. [Requirements](#requirements)
12. [Contributing](#contributing)
13. [License](#license)

## Project Structure

The project is organized with the following directory structure:

.
├── .devcontainer
│   ├── devcontainer.json
├── data
│   ├── base_result.csv
│   ├── cleaned_house_sales.csv
│   ├── compare_result.csv
│   ├── house_sales.csv
│   ├── processed_train_data.csv
│   ├── processed_train_df.csv
│   ├── processed_validation_data.csv
│   └── processed_validation_df.csv
├── cleaning_house_sales.py
├── data_mapper.py
├── house_sales_EDA.ipynb
├── profiling_house_sales_data.ipynb
├── requirements.txt
├── streamlit_app.py
├── train.py
└── validate.py


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   <!-- git clone https://github.com/your-username/your-repo.git -->


## Data

### Description

The datasets in the `data` folder serve various purposes in the house sales project. Here is a brief description of each:

- **base_result.csv**: Base result data.
- **cleaned_house_sales.csv**: Cleaned house sales data.
- **compare_result.csv**: Result comparison data.
- **house_sales.csv**: Raw house sales data.
- **processed_train_data.csv**: Processed training data.
- **processed_train_df.csv**: Processed training dataframe.
- **processed_validation_data.csv**: Processed validation data.
- **processed_validation_df.csv**: Processed validation dataframe.

### Data Details

- **house_sales.csv**: This file contains raw data related to house sales, including features such as price, location, and other relevant details.

- **cleaned_house_sales.csv**: After running the data cleaning script (`cleaning_house_sales.py`), this file is generated and contains the cleaned version of the house sales data.

- **processed_train_data.csv** and **processed_validation_data.csv**: These files contain the processed training and validation data, respectively, used for model training and validation.

- **compare_result.csv**: This file holds data for comparing results, possibly generated during model evaluation.

### Note

Ensure that you run the data cleaning script before using the processed data files.

...