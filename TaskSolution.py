import pandas

df1 = pandas.read_excel("1. Task Province.xlsx")
df2 = pandas.read_excel("2. Task Data.xlsx")

# merging the files
df3 = pandas.merge(df1, df2, on="Task #", how="inner")

df3.to_excel("Results.xlsx", index=False)
