
import pandas as pd

df = pd.read_csv('sales_data.csv')

df['Revenue'] = df['Quantity'] * df['Price']

totalRevenuePP = df.groupby('Product')['Revenue'].sum()

print("Total revenue per product:\n")
print(totalRevenuePP)
