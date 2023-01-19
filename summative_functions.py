import pandas as pd

import opendatasets as od

from glob import glob

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np


def import_data(path):
    '''
    Function to import the dataset from kaggle, it only accepts strings and file paths from kaggle
    It then uses the opendatasets function to download the file into the local folder before then using 
    the get_folder_name function to get the name of the newly created folder, next it uses glob to extract the
    file name and finally the data is imported as a pandas dataframe which is returned to the user
    '''
    if not isinstance(path, str): # input must be a string
        return print("Invalid input, file path must be a string")
    else:
        validator = URLValidator() #  create validator object

        try: # try catch statement to see if file path is valid
            validator(path)

            if "kaggle" not in path: # if the word kaggle isnt in the path then the path isnt to kaggle so is invalid
                return print("You must enter a url to a dataset within kaggle")
            else:

                try: # try catch incase there are other issues meaning the dataset cant be downloaded
                    od.download(path,force=True) # downloads the data from kaggle

                    folder = get_folder_name(path) # get the folder name
                    filename = glob("{}/*.csv".format(folder))[0] # get the file name
                    data = pd.read_csv(filename, index_col=0) # download the data as a pandas dataframe

                    return data
                except:
                    return print("Unable to download dataset")

                

        except ValidationError:
            return print("Invalid URL format")

        



    


def get_folder_name(path):
    '''
    Function which takes a string and finds all the text after the last backslash, this is the name of the folder created
    when data is imported from kaggle

    '''
    folder = path.split("/")[-1] # folder name will be after the last forwardslash
    return folder


def clean_col_names(df,new_col_names):
    '''
    Function which takes a dataframe, and a list of new column names to assign to it and changes all the column names. The dataframe must be a valid dataframe and columns must be a list
    where each item in the list is a string and the length of the list must be the same as the number of columns
    '''
    if not isinstance(df, pd.DataFrame): # must be a valid dataframe
        print("Invalid dataframe input, this is not a pandas dataframe")
    elif not isinstance(new_col_names, list): # must be a list
        print("You must enter a list object containing the names of the new columns")
    elif all(map(lambda x: isinstance(x, str), new_col_names)) is False: # each item in the list must be a string
        print("All items in the list of new names must be strings")
    elif len(df.columns) != len(new_col_names): # the number of items in the list must be the same as the number of dataframe columns
            print("The length of the list of new names must equal the number of columns in the data frame, which is {}".format(len(df.columns)))
    else: # all conditions met
        joined_dict = dict(zip(df.columns, new_col_names)) # create dictionary to map new names to old
        renamed_df = df.rename(columns = joined_dict) # rename columns
        return(renamed_df)




def create_boxenplots(data, col_names):

    '''
    Function to create boxenplots based on provided columns and dataframe, the dataframe must be a valid dataframe and columns must be a list
    where each item in the list is a string and each string is a valid name of a column in the dataframe, in addition the data type of each column
    must be int or float

    If all conditions are met then a boxenplot with a stripplot to add details is created for each column and added as a subplot to a main plot
    '''

    if not isinstance(data, pd.DataFrame): # must be a valid dataframe
        print("Invalid dataframe input, this is not a pandas dataframe")
    elif not isinstance(col_names, list): # must be a list
        print("You must enter a list object containing the names of columns you want to create boxenplots for")
    elif all(map(lambda x: isinstance(x, str), col_names)) is False: #  all items in the list must be strings
        print("All items in the list of column names must be strings")
    elif all(map(lambda x: x in data.columns, col_names)) is False: # all the strings in the list must be column names of the dataframe
        print("Invalid input must select valid column names")
    elif all(map(lambda x: data.dtypes[x] == np.int64 or data.dtypes[x] == np.float64 , col_names)) is False: # the data type of each column must be int or float
        print("Invalid input the data type of all columns must be numeric (int or float)")
    else: # all conditions passed so create the chart
        plt.rcParams["figure.figsize"] = (20,10) # size of figure

        fig, axes = plt.subplots(ncols=len(col_names)) # create plot and define number of subplots

        for col, ax in zip(col_names, axes): # for each column zip with an axes (subplot) and then loop over to generate the subplot
            sns.axes_style("ticks")
            sns.boxenplot(data = data[col], ax = ax) # create boxenplot
            sns.stripplot(data = data[col], ax = ax, color="red",size=2) # create stripplot
            ax.set_title(col) # add a title
            ax.tick_params(bottom = False, labelbottom =False) #  remove x axis ticks

        plt.show()



def create_count_plots(data,col_names):
    '''
    Funtion to create the countplots based on provided columns and a dataframe, the dataframe must be a valid dataframe and columns must be a list
    where each item in the list is a string and each string is a valid name of a column in the dataframe, in addition the data type of each column
    must be string

    If all conditons are met then a countplot is created for each column and added as a subplot to a main plot
    '''
    if not isinstance(data, pd.DataFrame): # must be a valid dataframe
        print("Invalid dataframe input, this is not a pandas dataframe")
    elif not isinstance(col_names, list): # must be a list
        print("You must enter a list object containing the names of columns you want to create count plots for")
    elif all(map(lambda x: isinstance(x, str), col_names)) is False: #  all items in the list must be strings
        print("All items in the list of column names must be strings")
    elif all(map(lambda x: x in data.columns, col_names)) is False: # all the strings in the list must be column names of the dataframe
        print("Invalid input must select valid column names")
    elif all(map(lambda x: data.dtypes[x] == object, col_names)) is False: # the data type of each column must be string (object)
        print("Invalid input the data type of all columns must be string")
    else: # all conditions passed so create the chart
        plt.rcParams["figure.figsize"] = (10,40) # size of figure
        fig, axes = plt.subplots(nrows=len(col_names))

        for col, ax in zip(col_names, axes): # for each column zip with an axes (subplot) and then loop over to generate the subplot
                    sns.axes_style("ticks")
                    sns.countplot(y = col, data = data, color="green", order = data[col].value_counts().index, ax = ax) # create count plot sorted by count
                    ax.set_title("Count plot: {}".format(col)) # add a title
                    ax.set(xlabel=None) # remove x label
                    ax.set(ylabel=None) #  remove y label

        plt.show()

def create_scatter_plots(data,value_1, value_2, hue_value):
    '''
    Funtion to create the scatter plots based on provided columns and a dataframe, here columns are provided as three seprerate varaibles, 
    the dataframe must be a valid dataframe and columns must be a string, where each is a valid name of a column in the dataframe, in addition the data type of the first two columns (value_1 and value_2)
    must be int or float while the value of the third must be a string

    If all conditons are met then a scatterplot is created for the given columns
    '''
    if not isinstance(data, pd.DataFrame): # must be a valid dataframe
        print("Invalid dataframe input, this is not a pandas dataframe")
    elif all(map(lambda x: isinstance(x, str), [value_1, value_2, hue_value])) is False: #  all column names must be strings
        print("All entered column names must be strings")
    elif all(map(lambda x: x in data.columns, [value_1, value_2, hue_value])) is False: # all the strings entered as column names must be column names of the dataframe
        print("Invalid input must enter valid column names")
    elif (all(map(lambda x: data.dtypes[x] == np.int64 or data.dtypes[x] == np.float64 , [value_1, value_2])) is False) or (data.dtypes[hue_value] != object): # the data type of value_1 and value_2 must be int or float and hue must be string
        print("Invalid input the data types of the two values must be int or float while the hue value must be a string")
    else: # all conditions passed so create the chart
        plt.rcParams["figure.figsize"] = (20,10) # size of figure
        sns.axes_style("ticks")
        chart = sns.scatterplot(data = data, x=value_1, y = value_2, hue=hue_value, s=100, marker = "D")
        chart.set_title("{} vs {}, with hue of {}".format(value_1, value_2, hue_value))
        plt.show()
