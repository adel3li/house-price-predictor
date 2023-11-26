# House Price Prediction Project

![banner](/img/cover.avif)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/semasuka/Loan-amount-prediction-regression)
![GitHub repo size](https://img.shields.io/github/repo-size/semasuka/Loan-amount-prediction-regression)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-Regression-red)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yejfDKFm8zRZ6swoEP-ibgx8ZOQe5vNl)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/semasuka/loan-amount-prediction-regression/main/loan_amount_app.py)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

Badge [source](https://shields.io/)

## Authors

- [@adel3li](https://github.com/adel3li)

## Description

This repository contains the code and data for a project related to house sales. The project involves data cleaning, exploratory data analysis (EDA), profiling, and model training and validation. The project is structured with specific folders for data, code, and various outputs.

## Table of Contents

1. [Repository Structure](#repository-structure)
2. [Installation](#installation)
3. [Data](#data)
4. [Code](#code)
5. [Data Profiling](#data-profiling)
6. [Data Cleaning](#data-cleaning)
7. [Exploratory Data Analysis](#exploratory-data-analysis)
8. [Model Training](#model-training)
10. [Validation](#validation)
11. [Streamlit App](#streamlit-app)
12. [Requirements](#requirements)
13. [Contributing](#contributing)
14. [License](#license)



## Repository structure

The Repository is organized with the following directory structure:

```
│
├── .devcontainer
│   ├── devcontainer.json                                 
│
│
├── datasets
│   ├── base_result.csv                                  
│   ├── cleaned_house_sales.csv                                 
│   ├── compare_result.csv                                  
│   ├── house_sales.csv                                 
│   ├── processed_train_data.csv                                  
│   ├── processed_train_df.csv                                 
│   ├── processed_validation_data.csv                                  
│   ├── processed_validation_df.csv                                
|
|
├── img
│   ├── 0.gif                              
│   ├── 1.gif                         
│   ├── 2.gif                         
│   ├── 3.gif                               
│   ├── 4.gif                   
│
│
├── notebooks
    ├── profiling_house_sales_data.ipynb.ipynb                  <- python notebook where all the data profiling are done.
    ├── house_sales_EDA.ipynb.ipynb                  <- main python notebook where all the analysis are done.
|
|
├── scripts
│   ├── app.py                              
│   ├── cleaning_house_sales.py                         
│   ├── data_mapper.py                         
│   ├── train.py                               
│   ├── validate.py                   
│
│
├── LICENSE                                       <- license file.
│
│
├── README.md                                     <- this readme file.
│
│
├── streamlit_app.py                            <- file with the model and streamlit component for rendering the interface.
│
│
├── requirements.txt                              <- list of all the dependencies with their versions(used for Streamlit).

```

<!-- - **.devcontainer**
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
  - `streamlit_app.py` -->


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/adel3li/house-sales.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repo
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


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

## Data Profiling

- **`notebooks/profiling_house_sales_data.ipynb`**
  - This Jupyter notebook profiles the house sales data, providing detailed statistics and information about the dataset.
  - It can be used to gain insights into the distribution of features and identify patterns.

## Data Cleaning

Data cleaning is a crucial step in preparing the house sales data for analysis and model training. The main data cleaning script is:

- **`scripts/cleaning_house_sales.py`**
  - This script is responsible for cleaning the raw house sales data.
  - It handles missing values, outliers, and other data inconsistencies to ensure the dataset is suitable for analysis and modeling.
  - The cleaned data is saved as `cleaned_house_sales.csv` in the `data` folder.


## Exploratory Data Analysis (EDA)

The exploratory data analysis is performed using Jupyter notebooks. Here is a brief overview of the EDA notebooks:

- **`notebooks/house_sales_EDA.ipynb`**
  - This Jupyter notebook explores the raw house sales data.
  - It contains visualizations, statistics, and insights to better understand the characteristics of the dataset.

## Model Training

Model training is a crucial step in developing a predictive model for house sales. The main script for training the model is:

- **`scripts/train.py`**
  - This script is responsible for training the machine learning model using the processed training data.
  - It may involve selecting a model, hyperparameter tuning, and fitting the model to the training data.
  - The trained model and relevant information are saved for later use.

  ## Model Validation

Model validation ensures that the trained machine learning model performs well on new, unseen data. The main script for model validation is:

- **`scripts/validate.py`**
  - This script is responsible for validating the trained model using the processed validation data.
  - It assesses the model's performance metrics, such as accuracy, precision, recall, and F1-score.
  - Validation results may be saved for further analysis and comparison.

  ## Streamlit App

A Streamlit web application is created to provide an interactive interface for visualizing data or model results. The main Streamlit app file is:

- **`app/streamlit_app.py`**
  - This script creates a web application using the Streamlit framework.
  - It may include interactive plots, charts, and other visualizations to showcase the project's findings or model predictions.
  - The app can be run using the following command:

    ```bash
    streamlit run app/streamlit_app.py
    ```

  - Access the app through the provided URL.

  <p align="center">
  <img src="/img/0.gif" alt="Streamlit App" width="800">
</p>

- Trying different number of bedrooms and house types.

<p align="center">
  <img src="/img/1.gif" alt="Streamlit App" width="800">
</p>

- Trying different Areas.

<p align="center">
  <img src="/img/2.gif" alt="Streamlit App" width="800">
</p>

- Trying different cities.

<p align="center">
  <img src="/img/3.gif" alt="Streamlit App" width="800">
</p>

- Trying different combinations.

<p align="center">
  <img src="/img/4.gif" alt="Streamlit App" width="800">
</p>

  ## Requirements

The project requires the following dependencies. Install them using the provided command:

- **Python 3.x**
  - Ensure you have Python 3.x installed on your system.

- **Dependencies**
  - Install the required Python packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

  - Check the `requirements.txt` file for a list of specific package versions used in the project.


## Contributing

contributions are welcomed to improve the project. To contribute, follow these steps:

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add your commit message here"
   ```
4. Push your changes to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

5. Open a pull request against the main repository.
6. Your pull request will be reviewed, and once approved, it will be merged.


### Bug Reports and Feature Requests

If you encounter any issues or have ideas for improvements, please open an issue on GitHub.

## MIT License

### Copyright (c) [2023] [Adel Ali]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.