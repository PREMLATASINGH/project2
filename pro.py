import numpy as np
import pandas as pd
data = {
    'customer_id': [1, 2, 3, 4, 5], 
    'purchase_amount': [100, 200, 150, 300, 250],
    'purchase_date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']),
    'product_category': ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
}
df = pd.DataFrame(data)
print(df)
print("\nSummary Statistics:")
print(df.describe())
print("\nData Types:")
print(df.dtypes)
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print(df.groupby('product_category')['purchase_amount'].mean())
print("\nTotal Purchase Amount by Product Category:")
total_purchase_by_category = df.groupby('product_category')['purchase_amount'].sum()
print(total_purchase_by_category)
print("\nTop 3 Customers by Purchase Amount:")
top_customers = df.nlargest(3, 'purchase_amount')
print(top_customers)
print("\nCustomers with Purchase Amount Greater than 200:")
high_value_customers = df[df['purchase_amount'] > 200]
print(high_value_customers)
print("\nCustomers Sorted by Purchase Amount:")
sorted_customers = df.sort_values(by='purchase_amount', ascending=False)
print(sorted_customers)
print("\nCustomers with Purchase Amount Between 150 and 250:")
mid_value_customers = df[(df['purchase_amount'] >= 150) & (df['purchase_amount'] <= 250)]
print(mid_value_customers)
print("\nCustomers with Purchase Amount Less than 150:")
low_value_customers = df[df['purchase_amount'] < 150]
print(low_value_customers)
print("\nCustomers with Purchase Amount Greater than 200 and in Electronics Category:")
electronics_high_value_customers = df[(df['purchase_amount'] > 200) & (df['product_category'] == 'Electronics')]
print(electronics_high_value_customers)
print("\nCustomers with Purchase Amount Less than 200 and in Clothing Category:")
print(df[(df['purchase_amount'] < 200) & (df['product_category'] == 'Clothing')])