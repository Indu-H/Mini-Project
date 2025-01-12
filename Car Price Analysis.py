  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  # Load the dataset
  df = pd.read_csv('price.csv')
  # Basic data inspection
  print(df.head())
  print(df.describe())
  # Analyze price distribution
  plt.figure(figsize=(10, 6))
  plt.hist(df['Price'], bins=20, edgecolor='black')
  plt.title('Car Price Distribution')
  plt.xlabel('Price')
  plt.ylabel('Frequency')
  plt.show()
 # Analyze price by car make
 avg_price_by_make = df.groupby('Make')['Price'].mean().sort_values()
 plt.figure(figsize=(12, 8))
 avg_price_by_make.plot(kind='barh')
 plt.title('Average Car Price by Make')
 plt.xlabel('Average Price')
 plt.ylabel('Car Make')
 plt.show()
 # Analyze price by year
 avg_price_by_year = df.groupby('Year')['Price'].mean()
 plt.figure(figsize=(10, 6))
 avg_price_by_year.plot(kind='line', marker='o')
 plt.title('Average Car Price by Year')
 plt.xlabel('Year')
 plt.ylabel('Average Price')
 plt.grid(True)
 plt.show()
