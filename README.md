# House Sales Project

## Description

This repository contains the code and data for a project related to house sales. The project involves data cleaning, exploratory data analysis (EDA), profiling, and model training and validation. The project is structured with specific folders for data, code, and various outputs.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Data](#data)
5. [Code](#code)
6. [Data Cleaning](#data-cleaning)
7. [Exploratory Data Analysis](#exploratory-data-analysis)
. [Model Training](#model-training)
10. [Validation](#validation)
11. [Streamlit App](#streamlit-app)
12. [Requirements](#requirements)
13. [Contributing](#contributing)
14. [License](#license)

## Project Structure

The project is organized with the following directory structure:

- **.devcontainer**
  - `devcontainer.json`

- **data**
  - `base_result.csv`
  - `cleaned_house_sales.csv`
  - `compare_result.csv`
  - `house_sales.csv`
  - `processed_train_data.csv`
  - `processed_train_df.csv`
  - `processed_validation_data.csv`
  - `processed_validation_df.csv`

- **scripts**
  - `cleaning_house_sales.py`
  - `data_mapper.py`
  - `train.py`
  - `validate.py`

- **notebooks**
  - `house_sales_EDA.ipynb`
  - `profiling_house_sales_data.ipynb`

- **requirements**
  - `requirements.txt`

- **app**
  - `streamlit_app.py`


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   <!-- git clone https://github.com/your-username/your-repo.git -->

  ```bash
  cd your-repo

  ```bash
  pip install -r requirements.txt


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

## Code

The code for this project is organized into scripts and notebooks. Below is an overview of the main code files:

- **Scripts:**
  - `cleaning_house_sales.py`: Script for cleaning house sales data.
  - `data_mapper.py`: Script for mapping data.
  - `train.py`: Script for model training.
  - `validate.py`: Script for model validation.

- **Notebooks:**
  - `house_sales_EDA.ipynb`: Jupyter notebook for exploratory data analysis.
  - `profiling_house_sales_data.ipynb`: Jupyter notebook for profiling house sales data.

## Data Cleaning

Data cleaning is a crucial step in preparing the house sales data for analysis and model training. The main data cleaning script is:

- **`scripts/cleaning_house_sales.py`**
  - This script is responsible for cleaning the raw house sales data.
  - It handles missing values, outliers, and other data inconsistencies to ensure the dataset is suitable for analysis and modeling.
  - The cleaned data is saved as `cleaned_house_sales.csv` in the `data` folder.


## Exploratory Data Analysis (EDA)

The exploratory data analysis is performed using Jupyter notebooks. Here is a brief overview of the EDA notebooks:

- **`notebooks/profiling_house_sales_data.ipynb`**
  - This Jupyter notebook profiles the house sales data, providing detailed statistics and information about the dataset.
  - It can be used to gain insights into the distribution of features and identify patterns.


- **`notebooks/house_sales_EDA.ipynb`**
  - This Jupyter notebook explores the raw house sales data.
  - It contains visualizations, statistics, and insights to better understand the characteristics of the dataset.


