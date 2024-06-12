import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class ProgrammingLanguage:
    # Initializes the class with an empty DataFrame
    def __init__(self):
        self.df = pd.DataFrame()
    
    def read_data(self, file):
        # Reads data from the specified file
        self.df = pd.read_csv(file)
        # Filters the data to only include programming languages of type 'pl'
        self.df = self.df.query("type == 'pl'")
        # Selects specific columns
        self.df = self.df[['pldb_id', 'type', 'appeared', 'number_of_users', 'number_of_jobs', 'is_open_source']]
        
    def calculate_counts(self, col):
        # Calculates and returns the value counts for the specified column
        return self.df[col].value_counts()
    
    # Generates a plot with the specified x and y parameters
    def generate_plot(self,col_x,col_y):
        plt.rcParams["figure.figsize"]=(10,5)
        fig=sns.scatterplot(x=col_x,y=col_y,data=self.df,color='#5E3C99',s=100)
        fig.tick_params(axis='both',which='major',labelsize=12)
        return fig
