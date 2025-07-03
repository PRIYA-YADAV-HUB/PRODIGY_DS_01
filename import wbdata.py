import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# List of countries
countries = ['IN', 'CN', 'US', 'BR', 'RU', 'ZA']

# Indicator: Total Population
indicator = {"SP.POP.TOTL": "Total Population"}

# Fetch the most recent data
df = wbdata.get_dataframe(indicator, country=countries)

# Clean it
df = df.reset_index()
df = df.sort_values(by='Total Population', ascending=False)

# Plot
plt.figure(figsize=(10, 6))
plt.bar(df['country'], df['Total Population'], color='skyblue')
plt.title('Latest Total Population by Country')
plt.xlabel('Country')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()