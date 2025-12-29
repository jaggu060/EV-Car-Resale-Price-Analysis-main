import matplotlib.pyplot as plt
import seaborn as sns
import re

plt.figure(figsize = (10,8))
sns.countplot(y = 'resale_price',data = filtered_data,order = filtered_data['resale_price'].value_counts().index[:10])
plt.title('Top 10 resale price')
plt.show()

sns.countplot(x = 'registered_year',data = filtered_data,order = filtered_data['registered_year'].value_counts().index[:10])
plt.title('Year of Registration')
plt.show()

sns.histplot(filtered_data['engine_capacity'], bins = 30, kde = True)
plt.title('Engine Capacity')
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.regplot(x = 'engine_capacity', y = 'resale_price', data = filtered_data, ax = axes[0,0], scatter_kws = {'alpha':0.3})
axes[0,0].set_title('Engine Capacity VS Resale Price')

sns.regplot(x = 'kms_driven', y = 'resale_price', data = filtered_data, ax = axes[0,1], scatter_kws = {'alpha':0.3})
axes[0,1].set_title('Kms Driven VS Resale Price')
axes[0,1].set_xscale('log')

sns.regplot(x = 'max_power', y = 'resale_price', data = filtered_data, ax = axes[1,0], scatter_kws = {'alpha':0.3})
axes[1,0].set_title('Max Power VS Resale Price')

for name, group in filtered_data.groupby('body_type'):
    sns.regplot(
        data=group, x='mileage', y='resale_price',
        ax=axes[1, 1],
        label=name,
        scatter_kws={'alpha':0.5},
        line_kws={'lw':1.5}
    )

axes[1, 1].legend(title='Body Type')
axes[1, 1].set_title("Mileage vs Resale Price by Body Type")

plt.tight_layout()
plt.show()

numeric_df = df_car.select_dtypes(include=['float64', 'int64'])
numeric_df = numeric_df.drop(columns = ['Unnamed: 0'])
plt.figure(figsize=(10,8))
sns.heatmap(numeric_df.corr(), annot = True, cmap = 'coolwarm')
plt.title('Feature correlation Heatmap')
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x = 'fuel_type', y = 'resale_price',data = filtered_data)
plt.title('Fuel Type VS Resale Price')
plt.show()

sns.boxplot(x = 'transmission_type', y = 'resale_price', data = filtered_data)
plt.title('Transmission Type VS Resale Price')
plt.show()