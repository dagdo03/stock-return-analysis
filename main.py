import matplotlib.pyplot as plt
import pandas as pd
import trendln
import numpy as np
import yfinance as yf

def identify_support_resistance(data):
    support_levels = []
    resistance_levels = []

    # Define the price data and indices
    prices = data['Close']
    indices = np.arange(len(prices))

    for i in range(1, len(prices) - 1):
        previous_price = prices[i - 1]
        current_price = prices[i]
        next_price = prices[i + 1]

        if previous_price > current_price < next_price:
            support_levels.append((indices[i], current_price))
        elif previous_price < current_price > next_price:
            resistance_levels.append((indices[i], current_price))

    return support_levels, resistance_levels


# Load your dataset
df = pd.read_csv('data/PTBA.csv')

# Convert the "Date" column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Sort the DataFrame by date if it's not already sorted
df = df.sort_values(by='Date')

# Filter data for the last 1 year
one_year_ago = df['Date'].max() - pd.DateOffset(years=1)
filtered_df = df[df['Date'] >= one_year_ago]
support_levels, resistance_levels = identify_support_resistance(df)

# Extract x and y coordinates for support and resistance lines
support_x, support_y = zip(*support_levels)
resistance_x, resistance_y = zip(*resistance_levels)

# Interpolate lines through support and resistance points
support_line = np.polyfit(support_x, support_y, 1)
resistance_line = np.polyfit(resistance_x, resistance_y, 1)

# Create a line plot of closing prices over the last 1 year
plt.figure(figsize=(12, 6))  # Adjust the figure size as needed
symbol = 'PTBA'
# Create the connecting line plot
plt.plot(filtered_df['Date'], filtered_df['Close'], label=symbol)
plt.plot(df.index[sorted(support_x)], np.polyval(support_line, sorted(support_x)), color='green', label='Support Line')
plt.plot(df.index[sorted(resistance_x)], np.polyval(resistance_line, sorted(resistance_x)), color='red', label='Resistance Line')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Closing Prices Over the Last 1 Year with Connecting Lines')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability if needed
plt.legend()  # Add a legend to the plot

# Show the plot
plt.tight_layout()  # Ensure that labels fit within the figure
plt.show()
