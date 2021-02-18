import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as plt # data visualization
#import matplotlib.pyplot as plt
import seaborn as sns #data visualization
import random

random.seed(1)
# Import the dataset
path="/home/pliu/data_set/argo_data_pipeline/pokemon-bad.csv"
pokemon = pd.read_csv(path)
# rename the column with a pound sign/hashtag as "number" its name
# The reason for this is when  we try and access this column later it will comment out the code
pokemon = pokemon.rename(index=str, columns={"#": "index"})
print(pokemon.head(15))