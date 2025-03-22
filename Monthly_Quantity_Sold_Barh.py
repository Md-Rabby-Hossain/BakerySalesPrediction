import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\pc\OneDrive\Desktop\PYTHON PROJECT\BakerySales.csv")

#Clean the dataset
data = data.drop(data.columns[0], axis = 1)
data["unit_price"]= data["unit_price"].str.rstrip("€")

#Change the datasets accordingly
data["unit_price"]=data["unit_price"].str.replace(",",".").astype(float)

data['date'] = pd.to_datetime(data['date'], format = 'mixed')
data['month'] = data['date'].dt.strftime('%B')
monthly_quantity = data.groupby('month')['Quantity'].sum()
month_order = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthly_quantity = monthly_quantity.reindex(month_order)

max_sales_month = monthly_quantity.idxmax()
max_sales_value = monthly_quantity.max()

plt.figure(figsize=(9,6)) #Figure size
bars = monthly_quantity.plot(kind='barh', color='skyblue') #Plot the figure with skyblue color

bars.patches[monthly_quantity.index.get_loc(max_sales_month)].set_color('red') #Change the color of max sold bar

for bar in bars.patches: # to show the quantity after each horizontal bar
    width = bar.get_width()
    plt.text(width+1, bar.get_y() + bar.get_height()/2,
        f'{int(width)}',
        va='center', fontsize=10, color='black')

plt.xlabel('Total Quantity Sold')
plt.ylabel('Month')
plt.title('Total Quantity Sold Per Month For The XYZ Bakery')
plt.gca().invert_yaxis() #To make the january at top
plt.savefig("MonthlyBakerySales.png") #to save the graph in the pc
plt.show()
