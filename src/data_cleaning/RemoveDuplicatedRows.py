#!/usr/bin/python

import sys
import pandas as pd
from string import Template


def remove_duplicated_rows(input_df):
    duplicate_row_df = input_df[input_df.duplicated()]
    duplicated_row_number=len(duplicate_row_df.index)
    if duplicated_row_number > 0:
        df_result = input_df.drop_duplicates()
    else:
        df_result = input_df
    return duplicated_row_number, df_result


if len(sys.argv) != 3:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    file_path = "/home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv"
    input_path = sys.argv[1]
    output_path=sys.argv[2]
    # print(path)
    input_df = pd.read_csv(input_path)
    result_str = '###################################################\n' \
                 '$duplicated_row_number duplicated lines has been removed from the data set in path:\n' \
                 '$input_path\n' \
                 '###################################################\n' \
                 'The cleaned data set is in path: $output_path\n' \
                 '###################################################\n'
    temp_obj = Template(result_str)
    duplicated_row_number, output_df = remove_duplicated_rows(input_df)
    output_df.to_csv(output_path,index=0)
    result = temp_obj.substitute(duplicated_row_number=duplicated_row_number, input_path=input_path,
                                 output_path=output_path)
    print(result)

# python RemoveDuplicatedRows.py /home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv /tmp/pokemon-dedup.csv