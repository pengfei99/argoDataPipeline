import pandas as pd
import numpy as np

series = [('Stranger Things', 3, 'Millie'),
          ('Game of Thrones', 8, 'Emilia'),
          ('La Casa De Papel', 4, 'Sergio'),
          ('Westworld', 3, 'Evan Rachel'),
          ('Stranger Things', 3, 'Millie'),
          ('La Casa De Papel', 4, 'Sergio')]

# Create a DataFrame object
df = pd.DataFrame(series, columns=['Name', 'Seasons', 'Actor'])
duplicated_element = df.duplicated()

# Find a duplicate rows
duplicateDFRow = df[duplicated_element]

print(duplicateDFRow)

df_final = df.drop_duplicates()
print(df_final.head())
df_final.to_csv('myfile.csv',index=False)

# duplicated_element_df=pd.DataFrame(duplicated_element,columns=['index','duplicated'])
# print(duplicated_element_df.head())
# for col in duplicated_element_df.columns:
#     print(col)

my_schema = {'index': np.int64,
             'Name': str,
             'Type_1': str,
             'Type_2': str,
             'Total': np.int64,
             'HP': np.int64,
             'Attack': np.int64,
             'Defense': np.int64,
             'Special_Attack': np.int64,
             'Special_Defence': np.int64,
             'Speed': np.int64,
             'Generation': np.int64,
             'Legendary': bool
             }
column_names = ['index',
                'Name',
                'Type_1'
                'Type_2'
                'Total',
                'HP',
                'Attack',
                'Defense',
                'Special_Attack',
                'Special_Defence',
                'Speed',
                'Generation',
                'Legendary']
