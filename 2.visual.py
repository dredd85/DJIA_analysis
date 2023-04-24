import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('DJIA.sqlite')
query = "SELECT strftime('%Y %m', Day) as Month, avg(Price) OVER(ORDER BY Day ROWS BETWEEN 25 PRECEDING AND CURRENT ROW ) as AVG, Price FROM stocks group by month"
data = pd.read_sql_query(query, conn)

plt.plot(data.Month, data.Price, data.AVG)
plt.title("Dija Stock")
plt.show()
conn.close()
