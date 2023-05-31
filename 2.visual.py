import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('DJIA.sqlite')
query = "SELECT strftime('%Y %m', Day) as Month, avg(Price) as Price FROM stocks GROUP BY Month"
df = pd.read_sql_query(query, conn)

ma_period25 = 25
ma_period50 = 50

# Convert 'Month' column to datetime format
df['Month'] = pd.to_datetime(df['Month']) 
df['MA25'] = df['Price'].rolling(window=ma_period25).mean()
df['MA50'] = df['Price'].rolling(window=ma_period50).mean()

plt.plot(df['Month'], df['Price'], label='Stock Price')
plt.plot(df['Month'], df['MA25'], label=f'{ma_period25}-Moving Average', color='red')
plt.plot(df['Month'], df['MA50'], label=f'{ma_period50}-Moving Average', color='green')

# Find the index of the annotation point
dotcom_bubble_burst_index = df[df['Month'].dt.year == 2000].index[0]
globa_financial_crisis_index = df[df['Month'].dt.year == 2008].index[0]

plt.annotate('Dot-com Bubble Burst', 
            xy=(df['Month'][dotcom_bubble_burst_index], df['Price'][dotcom_bubble_burst_index]),
            xytext=(df['Month'][dotcom_bubble_burst_index] - pd.DateOffset(years=6), df['Price'][dotcom_bubble_burst_index]+1000),
            arrowprops=dict(arrowstyle='->'))

plt.annotate('Global Finacial Criss', 
            xy=(df['Month'][globa_financial_crisis_index], df['Price'][globa_financial_crisis_index]+900),
            xytext=(df['Month'][globa_financial_crisis_index] - pd.DateOffset(years=7), df['Price'][globa_financial_crisis_index]+1500),
            arrowprops=dict(arrowstyle='->'))

plt.grid(True)
plt.xlabel('Years')
plt.xticks(df['Month'][::12], df['Month'].dt.year[::12], rotation=45)
plt.ylabel('Price')
plt.title('DJIA Stock Data with Moving Average')
plt.legend()

plt.show()
conn.close()