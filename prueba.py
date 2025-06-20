import pandas as pd
df = pd.read_csv("Mesas.csv")
print(df.to_string(index=False))