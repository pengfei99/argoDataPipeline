#!/usr/bin/python

import sys
import pandas as pd
from string import Template


def select_df_with_condition(input_df, col_name, condition):
    result_df = input_df[input_df[col_name] == condition]
    return result_df


if len(sys.argv) != 4:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    generated_file_name = sys.argv[3]
    input_df = pd.read_csv(input_path)
    for i in range(1, 7):
        output_df = select_df_with_condition(input_df, 'generation', i)
        head = output_df.head(5).to_string()
        output_file = output_path + "/" + generated_file_name+"-"+str(i)+".csv"
        output_df.to_csv(output_file, index=0)
        result_str = '###################################################\n' \
                     'Get generation $generation_num from the data set in path:\n' \
                     '$input_path\n' \
                     '###################################################\n' \
                     'The generated data set is in path: $output_file\n' \
                     '###################################################\n' \
                     'The head of the data set is : \n' \
                     '$head\n' \
                     '###################################################\n'
        temp_obj = Template(result_str)
        result = temp_obj.substitute(generation_num=1, input_path=input_path,
                                     output_file=output_file, head=head)
        print(result)

# python GeneratePokemonByGeneration.py /tmp/pokemon-enriched.csv /tmp pokemon-gen
