import pandas as pd

series = [('Stranger Things', 3, 'Millie'),
          ('Game of Thrones', 8, 'Emilia'),
          ('La Casa De Papel', 4, 'Sergio'),
          ('Westworld', 3, 'Evan Rachel'),
          ('Stranger Things', 3, 'Millie'),
          ('La Casa De Papel', 4, 'Sergio')]

# Create a DataFrame object
df = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])
duplicated_element=df.duplicated()

# Find a duplicate rows
duplicateDFRow = df[duplicated_element]

print(duplicateDFRow)

df_final=df.drop_duplicates()
print(df_final.head())


# duplicated_element_df=pd.DataFrame(duplicated_element,columns=['index','duplicated'])
# print(duplicated_element_df.head())
# for col in duplicated_element_df.columns:
#     print(col)