#!/usr/bin/python

import sys
import pandas as pd
from string import Template


def get_duplicated_rows(data_frame):
    duplicated_element = data_frame.duplicated()
    return data_frame[duplicated_element]


def get_duplicated_row_numbers(duplicate_row_df):
    return len(duplicate_row_df.index)


if len(sys.argv) != 3:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    # print(path)
    df = pd.read_csv(input_path, index_col=0)
    result_str = '###################################################\n' \
                 'The total number of duplicated rows is $duplicated_row_number\n' \
                 '###################################################\n' \
                 'The duplicated rows are: \n' \
                 '$duplicated_rows\n' \
                 '###################################################\n'
    temp_obj = Template(result_str)
    duplicated_rows = get_duplicated_rows(df)
    duplicated_row_numbers = get_duplicated_row_numbers(duplicated_rows)
    result = temp_obj.substitute(duplicated_row_number=duplicated_row_numbers,
                                 duplicated_rows=duplicated_rows.to_string())
    print(result)
    f = open(output_path, "w")
    if duplicated_row_numbers >= 1:
        f.write("True")
    else:
        f.write("False")
    f.close()

# python CheckDuplication.py /home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv /tmp/output_params.txt
