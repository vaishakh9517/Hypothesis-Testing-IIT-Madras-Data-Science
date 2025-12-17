#Hypothesis-Testing-on-Automotive-Pricing-Data

This repository contains a comprehensive statistical hypothesis testing project performed using Python, focused on validating business assumptions related to automotive pricing and vehicle characteristics.
The project demonstrates real-world application of inferential statistics to support data-driven decision-making.

The analysis includes:

One-Sample Hypothesis Tests (Mean & Proportion)

Two-Sample Hypothesis Tests (Mean & Proportion, including Welch’s t-test)

📁 Project Structure

/Hypothesis-Testing-on-Automotive-Pricing-Data/
│
├── Data/
│ └── Raw/
│ └── cars_sampled.csv
│
├── Notebooks/
│ └── hypothesis_testing_analysis.py
│
└── README.md

📊 Project Overview
🔍 Objective

To apply statistical hypothesis testing techniques on automotive market data in order to validate assumptions related to price trends, vehicle usage, fuel types, and transmission preferences.

This project simulates how analysts support business, pricing, and market strategy decisions using statistical evidence rather than intuition.

🧮 Data Summary

Source: Automotive dataset (used cars)

Key Features:

price

yearOfRegistration

kilometer

gearbox

fuelType

powerPS

Preprocessing:

Filtered invalid ranges for year, price, power, and mileage

Ensured realistic and business-relevant data bounds

Random sampling applied for hypothesis testing

📊 Analysis 1: One-Sample Hypothesis Testing
🔍 Business Questions

Has the average price of cars changed from a known historical benchmark?

Has the proportion of automatic transmission cars changed over time?

🛠️ Methodology

One-sample t-test for mean comparison

One-sample z-test for proportion comparison

Defined null and alternative hypotheses

Evaluated:

Test statistics

Critical values

p-values

Decision rules at α = 0.05

📈 Outcome

Statistical evidence showed no significant change in mean price and transmission proportion at the chosen significance level.

📊 Analysis 2: Two-Sample Hypothesis Testing
🔍 Business Questions

Do car prices differ significantly between different mileage ranges?

Has the proportion of petrol cars changed across different registration periods?

🛠️ Methodology

Variance comparison using F-test

Applied Welch’s t-test due to unequal variances

Two-sample z-test for proportion comparison

Calculated:

Degrees of freedom

Confidence intervals

Critical regions and p-values

📈 Outcome

Identified statistically significant differences in mean prices across mileage segments.

Found no significant change in petrol car proportions across time periods.

🧠 Statistical Concepts Applied

Hypothesis formulation (H₀ / H₁)

One-sample and two-sample testing

t-tests, z-tests, F-tests, Welch’s t-test

p-values and confidence intervals

Degrees of freedom

Statistical decision-making

🛠️ Tools & Technologies

Python

Pandas – data cleaning & manipulation

SciPy – statistical testing

Statsmodels – proportion tests

NumPy

Jupyter / Script-based analysis

✅ Skills Demonstrated

Statistical Analysis & Hypothesis Testing

Data Cleaning & Preprocessing

Inferential Statistics

Business Problem Translation into Statistical Tests

Analytical Thinking & Decision Validation

Python-based Data Analysis

📌 Conclusion

This project demonstrates how statistical hypothesis testing can be used to:

Validate or reject business assumptions

Support pricing and market decisions

Reduce decision-making bias using data

Apply theoretical statistics to real-world datasets