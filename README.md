# Summative assignment README

### Overview of the project

The project imports a dataset from kaggle, cleanses it using a number of functions, uses additional functions to create some new metrics and then finally displays the data in a variety of different charts.

The project is designed in python using both a python file to store the functions and a jupyter notebook to display all the data, in addition there is a python file used for testing the functions.

### Designing the charts

Figma was used to create a prototype of the notebook, to give an idea of how the notebook would be layed out and make creating the charts easier, this initial prototype was a wireframe and  can be seen below:

![Alt text](https://github.com/EDGENortheastern/owain_summative/blob/e91f25ff9e220dc7190a7ba37ad145b23ccf43fd/Wire%20frame%20-%20summative%201%20assignment.png)

Initially the data included on the charts was unknown as the data hadnt yet been analysed, but by creating an early prototype of what charts should be included it gave an early structure to the final product as well as a structure for which charts I should be aiming to make when looking at how the columns correlate to each other. After the analysis of the data was done a second protoype, also created in figma, was produced. The second version included what each chart would be showing and added some extra context to the various frames, this added detail should make the creation of the charts much easier. In addition the contents of the readme cells was added and some extra aspects such as cleaning the data and also the exact type of charts as for example the box plot was turned into a boxenplot with  a striplot overlayed.

![Alt text](https://github.com/EDGENortheastern/owain_summative/blob/b1cb2a9f3b09a596aedd1378b3906843f599b995/Wire%20frame%20-%20summative%201%20assignment%20(Copy).png)


### Project management

In order to ensure the project was kept on track and all tasks were completed, a ticketing system was used to create items on a kanban board, which is a project management tool designed to make it easier to track tasks by visually representing them on a board. The tasks can be moved across different sections as they are completed and even ranked in order of priority so that the key parts of a project in terms of impact are given the most time and man power. In the below images my kanban board can be seen in a couple of stages as the project developed.


Each item on the kanban board is a ticket which was rasied and represents a task that needs to be completed, they are given names, descriptions and labels to identofy what kind of task it is, meaning that different people within the project team can identify the tickets the need to work on more easily, this is also made easier by the fact that tickets can be assigned to individual or groups of people. The kanban board has 4 sections so that its easy to tack not only what the tasks are but also what stage of completion they are in. 

### The Code

#### Structure
The project consists of three main files, two python files which contain the functions and the tests and a jupyter notebook which the user will interact with in order to produce the charts.

#### Development
The project management method used to develop the project was agile project management, which is an iterative approach whereby tasks are completed in sprints or small stages, the advantage of this method over a more tradional linear method, such as the waterfall approach, is that testing occurs within each sprint iteration and therefore the tests are designed alongside the functions, the benefit of this method over the waterfall is that it can be faster as the tests are designed alongside the code and so this removes the need to wait until after the code is designed to start testing, it also means that as testing occurs alongside the development of the code that any bugs or issues will be spotted and fixed early and therefore there is less potential for them to impact the other functions later on. Another benefit of the agile methodolgy is that the exact requiments arent fixed, meaning that the exact types of charts being built could be modified as the process developed based on what was discovered about the data. An agile approach is also fits well with the use of a kanban board and ticketing sytem as at the start of each sprint the scrum master can decide which tickets they want to prioritise in that sprint.

#### Making the code user friendly
In order to make the code easy to understand and run comments were used throughout to explain what parts of the code were doing, the syntax of the code was kept consitent with varaibles given sensible descriptive names and finally doc strings were used to describe what each of the functions do, what their parameters are and what they return, this both makes the code easier to read but it also gives the user a way of finding out what a function does through the use of the help function, this can be seen in the image below.


#### Functions
The project has 6 different functions.

* get_folder_name - This function takes in a file path and uses the split function to find the name of a folder, it does this bases on the fact the folder name will be the last section after the last forward slash, this string is then returned by the function.

* import_data - This function is designed to import data from the kaggle website, it will only accept an input which is a string, and then also a valid filepath to kaggle if these conditions arent met then an error message is printed to the user but if they are then opendatasets package is used to download the data from kaggle, and then the get_folder_name function is used to find the folder name the data has been saved in, before the glob function is used to get the file name and finally the data is read in as a pandas dataframe and returned to the user.

* clean_col_names - This function changes the names of a dataframes columns based on a given list, the list must be the same length as the number of columns or an error is printed to the user.

* create_boxenplots - This function takes a dataframe and given list of columns and will create a plot containing a number of subplots whereby each subplot is a boxenplot with a stripplot overlayed on each of the given columns. The columns must be valid column names of the dataframe and also must be numeric columns, as you can't create a boxenplot of a string value. Finally, the chart is displayed to the user. 

* create_count_plots - This function takes a dataframe and given list of columns and will create a plot containing a number of subplots whereby each subplot is a countplot, the counts within the plot are ranked so that the value that appears most is at the top of the chart. The columns must be valid column names of the dataframe and also must be strings as this chart isn't designed for int or float values. Finally, the chart is displayed to the user. 

* create_scatter_plots - This function takes a dataframe and three strings, the strings represent column names of the dataframe. The first two columns are the x and y axis and so must be numeric values, while the third is the hue of the chart, or colour of the dots, and so the data in this column must be a string. If all the conditions are met then a scatterplot is created with the data and its displayed to the user.


