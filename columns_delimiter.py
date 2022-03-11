import pandas as pd
data = {"table_name": ['database.schema.name_table']}
df = pd.DataFrame(data)

df[['count_name_columns']] = df['table_name'].str.split('.', expand=True)
