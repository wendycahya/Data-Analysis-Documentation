import pandas as pd
df = pd.read_csv('comparison_3method.csv', sep='\s+', header=None)
df.to_csv('my_file.csv', header=None)