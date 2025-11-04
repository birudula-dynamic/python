# 4.1) ii) Convert a Pandas Series to a Python list
import pandas as pd

# Create a Pandas Series
series = pd.Series(['apple', 'banana', 'cherry', 'date'])

print(f"Original Pandas Series (type: {type(series)}):")
print(series)

# Convert the Series to a Python list
python_list = series.tolist()

print(f"\nConverted Python list (type: {type(python_list)}):")
print(python_list)

