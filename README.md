# Regression Project : Total Revolving Credit Prediction


# Acceptance criteria: 
To build the best model which should give the least possible RMSE  and the model should be deployed using Flask/Django/ RShiny/Heroku.

# Milestones: 
60 days to complete the Project.

# Process flow for the Project include below steps:-

## [1. Business Objective]
Revolving credit means you're borrowing against a line of credit. Let's say a lender extends a certain amount of credit to you, against which you can borrow repeatedly. The amount of credit you're allowed to use each month is your credit line, or credit limit. You're free to use as much or as little of that credit line as you wish on any purchase you could make with cash. Its just like a credit card and only difference is they have lower interest rate and they are secured by business assets.
At the end of each statement period, you receive a bill for the balance. If you don't pay it off in full, you carry the balance, or revolve it, over to the next month and pay interest on any remaining balance. As you pay down the balance, more of your credit line becomes available and usually its useful for small loans
As a bank or investor who are into this revolving balance here they can charge higher interest rates and convenience fees as there is lot of risk associated in customer paying the amount. Our company wants to predict the revolving balance maintained by the customer so that they can derive marketing strategies individually.

## [2. DataSet Details]
-The dataset is having Revolving Balance and associated Credit line attributes of customers. Which contains an event log extracted from Banking Sector.

-Dataset has 36 columns in total, in which 35 are Independent Variables and 'Tota_credit_revolving_balance' is Target Variable. 

[Dataset Details.xlsx](https://github.com/Shruti3893/Revolving_Credit-Regression-Project/blob/main/Dataset%20Details.xlsx) is the provided Dataset for the Project.

## [3. Exploratory Data Analysis]

### 1) Data Visualization:
- For getting Initial Overview of Dataset I choose to get Pandas Profiling Report. Below is the link for the same.

https://github.com/Shruti3893/Revolving_Credit-Regression-Project/blob/main/pandas_profiling_Report.html

- I performed complete Visualization in Tableau to get more deep hidden Insights. Below is the link for my Tableau workbook.

https://public.tableau.com/profile/shruti.bichkunde#!/vizhome/Revolving_Credit/PurposeandAnnualInc

### 2) Data Analysis:
- Missing Value Treatment:-
Data had lot of Missing Value Columns. I replaced missing values with Mean(), Median() or Mode() corresponding to their requirements.
- Outlier Treatment:-
We did Outlier Treatment via Capping and Flooring Approach. All the Outliers were mapped at 10% or 90% of min and max values.
- Data had no Duplicate Values. 

### 3) Feature Selection:
1. For selecting the desied features for final model, I tried various feature selection techniques, such as 
-Correlation
-Mutual info classif 
-Univariate Selection. 

2. I checked feature importance both graphically and analytically to come up with the list of desired columns for final model.

## [4. Model Building]
- I tried building various models with multiple algorithms such as 
1) Multi-Linear Regression
2) Multiple linear regression — least squares fitting
3) Polynomial Regression  
4) Random Forest Regressor
5) Decision Tree Regressor
6) Ridge Regression
7) Lasso Regression
8) Adaboost Algorithm
9) ElasticNet Regression

-Based on the Classification report, I choosed the best model as Decision Tree Regressor for the project. It gave least RMSE and comparatively high R1-score.

## [5. Deployment in Local System]
For Show casing the project, I used Django Framework.

## [6. Cloud Platform]
I deployed the final model on Heroku Cloud Platform. 

To see my website/web-api Go to >>> [https://revolving-credit.herokuapp.com/]
