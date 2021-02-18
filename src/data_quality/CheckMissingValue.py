#!/usr/bin/python

import sys
import pandas as pd
from string import Template

if len(sys.argv) != 2:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    file_path = "/home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv"
    path = sys.argv[1]
    # print(path)
    df = pd.read_csv(path, index_col=0)
    result_str = '###################################################\n'\
                 'The missing value per column is shown as followed\n' \
                 '$missing_value\n' \
                 '###################################################\n'
    temp_obj = Template(result_str)
    missing_value_df=df.isnull().sum()
    result = temp_obj.substitute(missing_value=missing_value_df.to_string())
    print(result)
