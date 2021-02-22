import sys
import pandas as pd
from string import Template


if len(sys.argv) != 2:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    file_path = "/home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv"
    path = sys.argv[1]
    # print(path)

    df = pd.read_csv(path)
    result_str = '###################################################\n' \
                 'The schema of this data set is shown as followed: \n' \
                 '$schema\n' \
                 '###################################################\n'
    temp_obj = Template(result_str)
    schema = df.dtypes
    # column_number=len(df.columns)
    # row_number=len(df)
    result = temp_obj.substitute(schema=schema)
    print(result)

