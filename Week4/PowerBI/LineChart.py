# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Profit, Date)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt
import pandas as pd

dataset['Date'] = pd.to_datetime(dataset['Date'])
dataset['Year-Month'] = dataset['Date'].dt.to_period('M')

monthly_data = dataset.groupby('Year-Month')['Profit'].sum().reset_index()
monthly_data['Year-Month'] = monthly_data['Year-Month'].dt.to_timestamp()

#plot data
plt.figure(figsize=(10,6))
plt.plot(monthly_data['Year-Month'],monthly_data['Profit'],marker='o',color='blue',label='Monthly Profit')
plt.title('Sum of Profit for Each Month',fontsize=16)
plt.xlabel('Month',fontsize=12)
plt.ylabel('Total Profit',fontsize=12)
plt.legend()

#Display the plot
plt.tight_layout()
plt.show()