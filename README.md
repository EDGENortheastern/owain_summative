# Summative assignment README

### Overview of the project

The project imports a dataset from kaggle, cleanses it using a number of functions, uses additional functions to create some new metrics and then finally displays the data in a variety of different charts.

The project is designed in python using both a python file to store the functions and a jupyter notebook to display all the data, in addition there is a python file used for testing the functions.

#### Workplace use case

The dataset being analysed by the project contains data on the uk mortgage market, information obtained from this datasource could be used for research wihtin my workplace or the data source itself could be used within dashboards or machine learning models. The functions are designed so that they can handle different data sets and so future use cases of this project could be that it acts as a pipeline for obtaining and then anaysing any data set on the kaggle website

### Designing the charts

Figma was used to create a prototype of the notebook, to give an idea of how the notebook would be layed out and make creating the charts easier, this initial prototype was a wireframe and  can be seen below:

![Image of Figma prototype 1](https://github.com/EDGENortheastern/owain_summative/blob/e91f25ff9e220dc7190a7ba37ad145b23ccf43fd/Wire%20frame%20-%20summative%201%20assignment.png)

Initially the data included on the charts was unknown as the data hadnt yet been analysed, but by creating an early prototype of what charts should be included it gave an early structure to the final product as well as a structure for which charts I should be aiming to make when looking at how the columns correlate to each other. After the analysis of the data was done a second protoype, also created in figma, was produced. The second version included what each chart would be showing and added some extra context to the various frames, this added detail should make the creation of the charts much easier. In addition the contents of the readme cells was added and some extra aspects such as cleaning the data and also the exact type of charts as for example the box plot was turned into a boxenplot with  a striplot overlayed. Finally, the analysis of the data revealed that it wouldnt be possible to do a time series with the avaiable data and so that section was removed.

![Image of Figma prototype 2](https://github.com/EDGENortheastern/owain_summative/blob/b1cb2a9f3b09a596aedd1378b3906843f599b995/Wire%20frame%20-%20summative%201%20assignment%20(Copy).png)


### Project management

Github was used as the primary project management tool for this project as not only did it allow for the changes to the code to be properly tracked through version control, but it also has other useful features such as a ticketing system, kanban board and the ability to create the readme file to document the project.

In order to ensure the project was kept on track and all tasks were completed, a ticketing system was used to create items on a kanban board, which is a project management tool designed to make it easier to track tasks by visually representing them on a board. The tasks can be moved across different sections as they are completed and even ranked in order of priority so that the key parts of a project in terms of impact are given the most time and man power. In the below images my kanban board can be seen in a couple of stages as the project developed.

#### First kanban board
This shows the kanban board during one of the first sprints, here the only tasks that had been completed where the creation of the readme file and the initial prototype.
![Image of kanban board 1](https://github.com/EDGENortheastern/owain_summative/blob/11844f0dc2d99c93e27d6465dc387b098bf0bed2/Kanban%20image%201.jpg)

#### Second kanban board
This shows the kanban board at a later stage during a different sprint when all the functions were being tested.
![Image of kanban board 2](https://github.com/EDGENortheastern/owain_summative/blob/a36e7345c74a29011aee2d83a8ad37ade114a617/Kanban%20image%202.jpg)

Each item on the kanban board is a ticket which was rasied and represents a task that needs to be completed, they are given names, descriptions and labels to identofy what kind of task it is, meaning that different people within the project team can identify the tickets the need to work on more easily, this is also made easier by the fact that tickets can be assigned to individual or groups of people. The kanban board has 4 sections so that its easy to tack not only what the tasks are but also what stage of completion they are in. 

### The Code

#### Structure
The project consists of three main files, two python files which contain the functions and the tests and a jupyter notebook which the user will interact with in order to produce the charts.

#### Development
The project management method used to develop the project was agile project management, which is an iterative approach whereby tasks are completed in sprints or small stages, the advantage of this method over a more tradional linear method, such as the waterfall approach, is that testing occurs within each sprint iteration and therefore the tests are designed alongside the functions, the benefit of this method over the waterfall is that it can be faster as the tests are designed alongside the code and so this removes the need to wait until after the code is designed to start testing, it also means that as testing occurs alongside the development of the code that any bugs or issues will be spotted and fixed early and therefore there is less potential for them to impact the other functions later on. Another benefit of the agile methodolgy is that the exact requiments arent fixed, meaning that the exact types of charts being built could be modified as the process developed based on what was discovered about the data. An agile approach is also fits well with the use of a kanban board and ticketing sytem as at the start of each sprint the scrum master can decide which tickets they want to prioritise in that sprint.

#### Making the code user friendly
In order to make the code easy to understand and run comments were used throughout to explain what parts of the code were doing, the syntax of the code was kept consitent with varaibles given sensible descriptive names and finally doc strings were used to describe what each of the functions do, what their parameters are and what they return, this both makes the code easier to read but it also gives the user a way of finding out what a function does through the use of the help function, this can be seen in the image below.

![Image of help function being demonstrated](https://github.com/EDGENortheastern/owain_summative/blob/a36e7345c74a29011aee2d83a8ad37ade114a617/Example%20of%20help%20function.jpg)


#### Functions
The project has 6 different functions.

* get_folder_name - This function takes in a file path and uses the split function to find the name of a folder, it does this bases on the fact the folder name will be the last section after the last forward slash, this string is then returned by the function.

* import_data - This function is designed to import data from the kaggle website, it will only accept an input which is a string, and then also a valid filepath to kaggle if these conditions arent met then an error message is printed to the user but if they are then opendatasets package is used to download the data from kaggle, and then the get_folder_name function is used to find the folder name the data has been saved in, before the glob function is used to get the file name and finally the data is read in as a pandas dataframe and returned to the user.

* clean_col_names - This function changes the names of a dataframes columns based on a given list, the list must be the same length as the number of columns or an error is printed to the user.

* create_boxenplots - This function takes a dataframe and given list of columns and will create a plot containing a number of subplots whereby each subplot is a boxenplot with a stripplot overlayed on each of the given columns. The columns must be valid column names of the dataframe and also must be numeric columns, as you can't create a boxenplot of a string value. Finally, the chart is displayed to the user. 

* create_count_plots - This function takes a dataframe and given list of columns and will create a plot containing a number of subplots whereby each subplot is a countplot, the counts within the plot are ranked so that the value that appears most is at the top of the chart. The columns must be valid column names of the dataframe and also must be strings as this chart isn't designed for int or float values. Finally, the chart is displayed to the user. 

* create_scatter_plots - This function takes a dataframe and three strings, the strings represent column names of the dataframe. The first two columns are the x and y axis and so must be numeric values, while the third is the hue of the chart, or colour of the dots, and so the data in this column must be a string. If all the conditions are met then a scatterplot is created with the data and its displayed to the user.

#### How to run the code

##### Packages
To run the code you must first ensure that all the required libraries are installed, the libraries used in this project are listed below.

* pandas - data manipulation library, which allows you to use data structures such as dataframes. Documentation found here: https://pandas.pydata.org/docs/

* opendatasets - designed to download online sources from kaggle and google drive. Documentation found here: https://pypi.org/project/opendatasets/

* glob - used for obtaining filenames from a folder. Documentation found here: https://docs.python.org/3/library/glob.html

* django - library designed to enable you to build websites with python, in this project is is used for validating that url's are valid. Documentation found here: https://docs.djangoproject.com/en/4.1/

* matplotlib - library designed for creating visualizations in python. Documentation found here: https://matplotlib.org/stable/index.html

* seaborn - library designed for enhancing matplotlib vizualisations. Documentation found here: https://seaborn.pydata.org/tutorial.html

* numpy - mathematical library which offers a number of mathematical functions as well as data structures such as matricies and arrays. Documentation found here: https://numpy.org/doc/stable/

##### Running the notebook
If all the packages are installed then the notebook can be run, it's designed so that the only required user inputs should be the username and key for the users kaggle account, if these are entered correctly then the rest of the notebook will run, displaying the charts to the user.

The functions are designed to be able to handle other datasets and also be able to create different charts based on what is input into them, so the notebook can be customised to display differnt datasets from kaggle and also show different charts too.

### Testing

#### Unit testing
In order to test the different functions the pytest package was used, this allows each individual function to be tested to make sure it outputs the required results and also doesnt allow invalid inputs

All the tests are contained in the test_summative_functions.py file and they can be run on the command line, the below image shows the output of the tests being run on the command line confirming they all passed.

Within the test file two fixtures were created, these are then used as inputs for some of the tests so that the same objects dont have to be created for each test, the first of these creates a dataframe and the second is a list of valid column names

Most of the tests are designed to ensure that if invalid data is input to the functions that nothing is returned, when the actual functions are run an error message is printed to the user but no object should actually be returned, there are also tests to check the logic is correct for when the inputs are valid as although you can't test whether a chart is correct you can test to check that if valid inputs were used that a chart would be created. 

The unit tests were designed alongside the actual functions so that it was confirmed that each function worked and so wouldn't cause any issues with other functions.

#### A/B testing
In order to get the appearance of the charts correct a/b testing was used to get input from potential end users on what the charts should look like, this feedback was used to determine the final design. This research was carried out through the google form linked here: https://forms.gle/tDtXaTMRjfCnCkdp9

The form was designed to get input on areas such as should the count plot be sorted and should it have different colour bars, and the feddback obtained from the survey gave an insight into how the charts should be designed in order to offer the most impact to the end users.

### Evaluation

Overall the project was a success as the final notebook works and looks as intended, as its able to read in data from kaggle and create a number of charts based on that data. In addition, the code is designed so that different data sources could be used and different columns within those data sources analysed, meaning that this project acts as a potential pipeline for analysing and creating charts on any data source on the kaggle website, this ability could be further adabpted to enable different kinds of charts such as time series or pie chart to be developed. 

The project management of the task also worked well. An agile approach meant that testing and devleopment of the code went hand in hand and therefore the unit tests developed were able to remove any issues and bugs before they could impact other functions, the ticketing system ensured that all tasks were completed in time and that no areas were neglected and finally the use of github meant that it was easy to track the different versions of the project and in some cases go back to previous versions if issues were discovered.

Finally, the code was well documented and tested meaning that issues were removed and that it's easy to understand what the different parts are doing, so if other people were to take over the project after its completion they should be able to understand what each functions purpose is.

The are a couple of areas where the project could be improved or enhanced, firstly a different visuallisation library such as plotly could be used to make the charts interactive, this may be useful for finding out more about the data and so improve the overall effectiveness of the project. Next, the ability to read in data could be extended beyond just kaggle, which would allow for a wider range of data to be analysed. And finally, the project could be moved to a web app through a pacvkage such as dash, this would likely make it more accessible to a wider range of users than a jupyter notebook as it would require any knowledge of python.

