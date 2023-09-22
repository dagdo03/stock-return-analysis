import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset
df = pd.read_csv('data/PTBA.csv')

# Convert the "Date" column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date if it's not already sorted
df = df.sort_values(by='Date')

# Filter data for the last 1 year
one_year_ago = df['Date'].max() - pd.DateOffset(years=1)
filtered_df = df[df['Date'] >= one_year_ago]

# Create a line plot of closing prices over the last 1 year
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

# Create the connecting line plot
plt.plot(filtered_df['Date'], filtered_df['Close'], marker='o', linestyle='-', color='orange', markersize=5, label='Connecting Lines')

plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Prices Over the Last 1 Year with Connecting Lines')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.legend()  # Add a legend to the plot

# Show the plot
plt.tight_layout()  # Ensure that labels fit within the figure
plt.show()
