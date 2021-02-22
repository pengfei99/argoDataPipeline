#!/usr/bin/python

import sys
import pandas as pd
from string import Template


def rename_column_names(input_df, column_rename_list):
    rename_col_size = len(column_rename_list)
    df_result = input_df.rename(index=str, columns=column_rename_list)
    return rename_col_size, df_result


if len(sys.argv) != 3:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    file_path = "/home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv"
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    # print(path)
    input_df = pd.read_csv(input_path)
    result_str = '###################################################\n' \
                 '$rename_col_size columns has been renamed from the data set in path:\n' \
                 '$input_path\n' \
                 '###################################################\n' \
                 'The new data set is in path: $output_path\n' \
                 '###################################################\n' \
                 'The head of the data set is : \n' \
                 '$head\n' \
                 '###################################################\n'
    temp_obj = Template(result_str)
    column_rename_list = {"#": "index",
                          "Name": "name",
                          "Type 1": "type_1",
                          "Type 2": "type_2",
                          "Total": "total",
                          "HP":"hp",
                          "Attack": "attack",
                          'Defense': "defense",
                          "Sp. Atk": "special_attack",
                          "Sp. Def": "special_defense",
                          'Speed': "speed",
                          'Generation': "generation",
                          'Legendary': "legendary"
                          }


    rename_col_size, output_df = rename_column_names(input_df, column_rename_list)
    output_df.to_csv(output_path, index=0)
    head = output_df.head(5).to_string()
    result = temp_obj.substitute(rename_col_size=rename_col_size, input_path=input_path,
                                 output_path=output_path, head=head)
    print(result)

# python RenameColumns.py /home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv /tmp/pokemon-cleaned.csv
