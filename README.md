📘 EV Car Resale Price Analysis

A complete exploratory data analysis (EDA) project focused on understanding the factors that impact resale prices of used cars in India.

🔍 Objectives

Clean raw car listing data

Standardize price formats (₹, lakhs, crores)

Transform text fields → numeric (mileage, engine capacity, power, km driven)

Remove outliers

Explore feature relationships

Identify strongest predictors of resale value

📂 Project Structure
EV-Car-Resale-Price-Analysis/
 ├── data/
 ├── notebook/
 ├── src/
 ├── images/
 └── README.md

📊 Key Insights
✔ Engine Capacity and Max Power

Strong positive correlation with resale value.

✔ Mileage

Negative correlation — higher mileage ↓ resale price.

✔ KMs Driven

Logarithmic drop-off: high km = steep price drop.

✔ Fuel Type

Diesel cars retain value significantly better than Petrol/CNG.

✔ Transmission

Automatic cars typically have a higher resale value.

✔ Cities

Tier-1 metro cities show the highest average resale prices.

📈 Sample Visuals
Plot	Description
Engine Capacity vs Price	Shows strong correlation
KMs Driven vs Price	Price drops sharply after a threshold
Fuel Type Boxplot	Diesel consistently highest
Correlation Heatmap	Identifies strongest predictors

Screenshots stored in /images/.

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Regex

Jupyter Notebook

🚀 How to Run

pip install -r requirements.txt
jupyter notebook

📢 About the Project

This project helps used-car sellers and buyers understand what drives resale value.
It also demonstrates strong skills in:

Data cleaning

Text → numeric conversion

EDA + visualization

Outlier detection

Feature correlation
