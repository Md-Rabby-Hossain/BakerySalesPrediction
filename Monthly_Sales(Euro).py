import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"C:\Users\pc\OneDrive\Desktop\python practice\CleanedBakerySales.csv")

data['date'] = pd.to_datetime(data['date'], format = 'mixed')
data['month'] = data['date'].dt.strftime('%B')
monthly_sales = data.groupby('month', observed=True)['unit_price'].sum().reset_index()

max_month = monthly_sales['unit_price'].idxmax()
max_sales = monthly_sales.loc[max_month, 'unit_price']

plt.figure(figsize=(10,6))
bars = plt.barh(monthly_sales['month'].astype(str), monthly_sales['unit_price'], color = 'blue')

bars[max_month].set_color('red')

for bar in bars:
    width = bar.get_width()
    plt.text(width,
             bar.get_y()+bar.get_height()/2,
             f'{int(width)}',
             va = 'center',
             ha = 'left',
             fontsize=12)

plt.xlabel('Sales(€)')
plt.ylabel('Month')
plt.title('Total Sales(in €) Of Each Month')
plt.show()
