import duckdb
import pandas as pd

emp_path = r"D:\DataMax\Data\emp.csv"
df  = pd.read_csv(emp_path)

df_count = duckdb.sql("select count(1) from df")
df_count =df_count.to_df()
print(df_count)

