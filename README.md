# Rossmann Pharmaceuticals Sales Forecasting Challenge

## Overview
This project aims to forecast sales for Rossmann Pharmaceuticals stores across several cities, six weeks ahead of time. The finance team relies on these predictions to plan and make informed decisions. The project involves data cleaning, exploratory data analysis (EDA), machine learning, and deep learning techniques to build and serve an end-to-end product for sales prediction.

## Business Need
Managers in individual stores currently use their experience and judgment to forecast sales. The data team has identified factors such as promotions, competition, school and state holidays, seasonality, and locality as crucial for predicting sales. Our goal is to leverage these factors to build a robust sales forecasting model.

## Data and Features
The dataset includes the following fields:
- **Id**: Represents a (Store, Date) duple within the test set.
- **Store**: Unique ID for each store.
- **Sales**: Turnover for any given day (target variable).
- **Customers**: Number of customers on a given day.
- **Open**: Indicator for whether the store was open (0 = closed, 1 = open).
- **StateHoliday**: Indicates a state holiday (a = public holiday, b = Easter holiday, c = Christmas, 0 = None).
- **SchoolHoliday**: Indicates if the (Store, Date) was affected by the closure of public schools.
- **StoreType**: Differentiates between 4 different store models (a, b, c, d).
- **Assortment**: Describes an assortment level (a = basic, b = extra, c = extended).
- **CompetitionDistance**: Distance in meters to the nearest competitor store.
- **CompetitionOpenSince[Month/Year]**: Approximate year and month when the nearest competitor was opened.
- **Promo**: Indicates whether a store is running a promo on that day.
- **Promo2**: Continuing and consecutive promotion for some stores (0 = store is not participating, 1 = store is participating).
- **Promo2Since[Year/Week]**: Year and calendar week when the store started participating in Promo2.
- **PromoInterval**: Consecutive intervals Promo2 is started (e.g., "Feb, May, Aug, Nov").

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository
```bash
git clone https://github.com/zol23-g/Sales_Forecasting_Rossmann_Pharmaceuticals.git
cd Sales_Forecasting_Rossmann_Pharmaceuticals  

### Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
### Install Dependencies
pip install -r requirements.txt
