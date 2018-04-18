import pandas as pd

from survey_data_dictionary_testing import DATA_DICTIONARY

# Load data

# We want to take the names list from our data dictionary
names = [x.name for x in DATA_DICTIONARY]

df = pd.read_csv('data/survey.csv', names=names, header=0)