import pandas as pd
import os

# Create dataFrame with column names
data = {'Name': ['Tom', 'nick', 'krish', 'jack'],
        'Age': [20, 21, 19, 18],
        'City' : ['New York', 'Los Angeles', 'Chicago', 'Houston']
        }

df = pd.DataFrame(data)

# Adding new row to df for ver2
new_row = {'Name': 'Anna', 'Age': 22, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

# Adding new row to df for ver3
new_row = {'Name': 'hari', 'Age': 25, 'City': 'San Francisco'}
df.loc[len(df)] = new_row

# Ensuring "data" directory exists at root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample.csv")
df.to_csv(file_path, index=False)
print(f"DataFrame saved to {file_path}")