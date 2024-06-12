import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pytest
from data_analysis import ProgrammingLanguage


#def test_ProgrammingLanguage():
#    out = ProgrammingLanguage()
#    assert type(out) == ProgrammingLanguage
#    assert out.df
#    assert type(out.df) == pd.core.frame.DataFrame

def test_read_data():
    lang = ProgrammingLanguage()
    lang.read_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-03-21/languages.csv')
    
    assert lang.df.shape == (3368, 6)
    assert 'number_of_users' in lang.df.columns
    assert 'number_of_jobs' in lang.df.columns
    
def test_calculate_counts():
    lang = ProgrammingLanguage()
    lang.read_data('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-03-21/languages.csv')
    
    counter = lang.calculate_counts(col='is_open_source')
    
    assert counter[True] == 328
    assert counter[False] == 56
    assert 'is_open_source' in lang.df.columns
    
    
