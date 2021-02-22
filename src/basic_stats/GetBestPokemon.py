#!/usr/bin/python

import sys
import pandas as pd
from string import Template


def get_best_pokemon(input_df, length):
    input_df.sort_values(by=['mod_stats'], inplace=True, ascending=False)
    result_df = input_df.head(length)
    print(result_df)


if len(sys.argv) != 2:
    print('Number of arguments that you give is wrong, please enter the path of the file which you want to analyze.')
else:
    input_path = sys.argv[1]
    input_df = pd.read_csv(input_path)
    get_best_pokemon(input_df, 5)

# python GetBestPokemon.py /tmp/pokemon-enriched.csv
# python GetBestPokemon.py /tmp/pokemon-gen-4.csv