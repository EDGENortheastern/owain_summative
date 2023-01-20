# Summative assignment - Analysis of the UK mortgage market dataset 

### Overview of the project 

The project imports a dataset from Kaggle, cleanses it using a number of functions and then displays the data in a variety of different charts, using custom made functions for each chart type. 

The project is designed in python using a python file to store the functions and a Jupyter notebook to display all the data, in addition there is a python file used for testing the functions. 

#### Workplace use case 

The dataset being analysed by the project contains data on the Uk mortgage market, information obtained from this data source could be used for research within my workplace or the data source itself could be used within dashboards or machine learning models, with the analysis of the dataset in this project revealing how it should be used. The functions are designed so that they can handle different data sets and so future use cases of this project could be that it acts as a pipeline for obtaining and then analysing any data set on the Kaggle website.

The dataset used in this project can be found here [Uk mortgage rates kaggle page](https://www.kaggle.com/datasets/thedevastator/uk-mortgage-rates-thousands-of-mortgage-products)

### Designing the charts 

Figma was used to create a prototype of the notebook, to give an idea of how the notebook would be laid out, therefore making the creation of the charts easier, the initial prototype was a wireframe and can be seen below: 

![Image of Figma prototype 1](https://github.com/EDGENortheastern/owain_summative/blob/e91f25ff9e220dc7190a7ba37ad145b23ccf43fd/Wire%20frame%20-%20summative%201%20assignment.png) 

Initially, the data included on the charts was unknown as the data hadn't yet been analysed, but by creating an early prototype of what charts should be included it gave an early structure to the final product as well as a structure for which charts, I should be aiming to make when looking at how the columns correlate to each other. In addition, it meant an initial design could be presented to stakeholders in order to obtain feedback on what the project should include. 

After the analysis of the data was done a second prototype, also created in Figma, was produced. The second version included what each chart would be showing and added some extra context to the various frames, this added detail should make the creation of the charts much easier. In addition, the contents of the readme cells was added and some extra aspects such as cleaning the data and also the exact type of charts as for example the box plot was turned into a boxenplot with a stripplot overlayed. Finally, the analysis of the data revealed that it wouldn't be possible to do a time series with the available data and so that section was removed. 

![Image of Figma prototype 2](https://github.com/EDGENortheastern/owain_summative/blob/b1cb2a9f3b09a596aedd1378b3906843f599b995/Wire%20frame%20-%20summative%201%20assignment%20(Copy).png) 

### Project management 

GitHub was used as the primary project management tool for this project as not only did it allow for the changes to the code to be properly tracked through version control, but it also has other useful features such as a ticketing system, Kanban board and the ability to create the readme file to document the project. 

In order to ensure the project was kept on track and all tasks were completed, a ticketing system was used to create items on a Kanban board, which is a project management tool designed to make it easier to track tasks by visually representing them on a board. The tasks can be moved across different sections as they are completed and even ranked in order of priority so that the key parts of a project in terms of impact are given the most time and man power. In the images below the Kanban board for this project can be seen in a couple of stages as the project developed. 

#### First Kanban board 

This shows the Kanban board during one of the first sprints, here the only tasks that had been completed where the creation of the readme file and the initial prototype. 

![Image of Kanban board 1](https://github.com/EDGENortheastern/owain_summative/blob/11844f0dc2d99c93e27d6465dc387b098bf0bed2/Kanban%20image%201.jpg) 

#### Second Kanban board 

This shows the Kanban board at a later stage during a different sprint when all the functions were being tested. 

![Image of Kanban board 2](https://github.com/EDGENortheastern/owain_summative/blob/a36e7345c74a29011aee2d83a8ad37ade114a617/Kanban%20image%202.jpg) 

Each item on the Kanban board is a ticket which was raised and represents a task that needs to be completed, they are given names, descriptions and labels to identify what kind of task it is, meaning that different people within the project team can identify the tickets the need to work on more easily, this is also made easier by the fact that tickets can be assigned to an individual or groups of people. The Kanban board has 4 sections so that it's easy to track not only what the tasks are but also what stage of completion they are in.  

### The Code 

#### Structure 

The project consists of three main files, two python files which contain the functions and the tests and a Jupyter notebook which the user will interact with in order to produce the charts. 

#### Development 

The project management method used to develop the project was agile project management, which is an iterative approach whereby tasks are completed in sprints or small stages, the advantage of this method over a more traditional linear method, such as the waterfall approach, is that testing occurs within each sprint iteration and therefore the tests are designed alongside the functions, when compared to the waterfall this means that the project duration should be faster as the tests are designed alongside the code and so this removes the need to wait until after the code is designed to start testing, it also means that testing occurs alongside the development of the code, so any bugs or issues will be spotted and fixed early and therefore there is less potential for them to impact the other functions later on. Another benefit of the agile methodology, is that the exact requirements aren't fixed, meaning that the exact types of charts being built could be modified as the process developed based on what was discovered about the data. An agile approach also suits the use of a Kanban board and ticketing system as at the start of each sprint the scrum master can decide which tickets they want to prioritise in that sprint, with the Kanban board allowing the team to track task completion during the sprint. 

#### Making the code user friendly 

In order to make the code easy to understand and run, comments were used throughout to explain what sections of the code were doing, the syntax of the code was kept consistent with variables given sensible descriptive names, and snake case used throughout. Finally, doc strings were used to describe what each of the functions do, what their parameters are and what they return, this makes the code easier to read, and also gives the user a way of finding out what a function does through the use of the help function, this can be seen in the image below. 

![Image of help function being demonstrated](https://github.com/EDGENortheastern/owain_summative/blob/a36e7345c74a29011aee2d83a8ad37ade114a617/Example%20of%20help%20function.jpg) 

#### Functions 

The project has 6 different functions, descriptions of what each of them does can be seen below. 

* get_folder_name - This function takes in a file path and uses the split function to find the name of a folder, it does this based on the fact the folder name will be the last section after the last forward slash, this string is then returned by the function, as this function is used within the import_data function, it assumes its input is valid as the import_data function handles any scenarios this function wouldn’t be able to handle.  

* import_data - This function is designed to import data from the Kaggle website, it will only accept an input which is a string, and then also a valid file path to Kaggle. If these conditions aren't met then an error message is printed to the user, but if they are then opendatasets package is used to download the data from Kaggle, and then the get_folder_name function is used to find the folder name the data has been saved in, before the glob function is used to get the file name and finally, the data is read in as a pandas data frame and returned to the user. 

* clean_col_names - This function changes the names of a data frames columns based on a given list, the list must be the same length as the number of columns or an error is printed to the user. 

* create_boxenplots - This function takes a data frame and given list of columns and will create a plot containing a number of subplots whereby each subplot is a boxenplot with a stripplot overlayed, it does this for each of the given columns. The columns must be valid column name of the data frame and also must be numeric columns, as you can't create a boxenplot of a string value. Finally, the chart is displayed to the user.  

* create_count_plots - This function takes a data frame and given list of columns and will create a plot containing a number of subplots, whereby each subplot is a countplot, the counts within the plot are ranked so that the value that appears most often is at the top of the chart. The columns must be valid column names of the data frame and also must be strings as this chart isn't designed for int or float values. Finally, the chart is displayed to the user.  

* create_scatter_plots - This function takes a data frame and three strings; the strings represent column names of the data frame. The first two columns are the x and y axis of the chart and so must be numeric values, while the third is the hue of the chart, or colour of the dots, and so the data in this column must be a string. If all the conditions are met then a scatterplot is created with the data and it is displayed to the user. 

#### How to run the code 

##### Packages 

To run the code, you must first ensure that all the required libraries are installed, the libraries used in this project are listed below. 

* pandas - data manipulation library, which allows you to use data structures such as data frames. Documentation found here: [pandas documentation](https://pandas.pydata.org/docs/) 

* opendatasets - designed to download online sources from Kaggle and google drive. Documentation found here: [opendatasets documentation](https://pypi.org/project/opendatasets/)

* glob - used for obtaining filenames from a folder. Documentation found here: [glob documentation](https://docs.python.org/3/library/glob.html) 

* django - library designed to enable you to build websites with python, in this project it is used for validating that URL's are valid. Documentation found here: [django documentation](https://docs.djangoproject.com/en/4.1/)

* matplotlib - library designed for creating visualizations in python. Documentation found here: [matplotlib documentation](https://matplotlib.org/stable/index.html) 

* seaborn - library designed for enhancing matplotlib visualisations. Documentation found here: [seaborn documentation](https://seaborn.pydata.org/tutorial.html) 

* numpy - mathematical library which offers a number of mathematical functions as well as data structures such as matrices and arrays. Documentation found here: [numpy documentation](https://numpy.org/doc/stable/)

* pytest - testing library for python, providing the ability to unit test functions. Documentation found here: [pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)

##### Running the notebook 

If all the packages are installed then the notebook can be run, it's designed so that the only required user inputs should be the username and key for the users Kaggle account, if these are entered correctly then the rest of the notebook will run, displaying the charts to the user. 

The functions are designed to be able to handle other datasets and also be able to create different charts based on what is input into them, so the notebook can be customised to display different datasets from Kaggle and also show different charts too. 

### Testing 

#### Unit testing 

In order to test the different functions, the pytest package was used, this allows each individual function to be tested to make sure it outputs the required results and also doesn't allow invalid inputs 

All the tests are contained in the test_summative_functions.py file and they can be run on the command line; the below image shows the output of the tests being run on the command line confirming they all passed. 

![Image of pytest being run](https://github.com/EDGENortheastern/owain_summative/blob/805260cd49aff8b842e3d65829cdbe913b56ca7e/Example%20of%20pytest%20being%20run.jpg) 

Within the test file two fixtures were created, these are then used as inputs for some of the tests so that the same objects don't have to be created for each test, the first of these creates a data frame and the second is a list of valid column names 

Most of the tests are designed to ensure that if invalid data is input to the functions, then nothing is returned, when the actual functions are run an error message is printed to the user but no object should actually be returned, there are also tests to check the logic is correct for when the inputs are valid as although you can't test whether a chart is correct you can test to check that if valid inputs were used that a chart would be created.  

The unit tests were designed alongside the actual functions so that it was confirmed that each function worked, and therefore wouldn't cause any issues with other functions. 

#### A/B testing 

In order to get the appearance of the charts correct a/b testing was used to get input from potential end users on what the charts should look like, this feedback was used to determine the final design. This research was carried out through the google form linked here: [A/B testing google docs form](https://forms.gle/tDtXaTMRjfCnCkdp9)

The form was designed to get input on areas such as: should the count plot be sorted; and should it have different colour bars. The feedback obtained from the survey gave an insight into how the charts should be designed in order to offer the most impact to the end users. 

### Evaluation 

Overall, the project was a success as the final notebook works and looks as it was designed too. It is able to read in data from Kaggle and create a number of charts based on that data. In addition, the code is designed so that different data sources could be used and different columns within those data sources analysed, meaning that this project acts as a potential pipeline for analysing and creating charts on any data source found on the Kaggle website, this ability could be further adapted to enable different kinds of charts such as line or pie charts to be developed.  

The project management of the task also worked well. An agile approach meant that testing and development of the code went hand in hand and therefore the unit tests developed were able to remove any issues and bugs before they could impact other functions, the ticketing system ensured that all tasks were completed in time and that no areas were neglected and finally, the use of GitHub meant that it was easy to track the different versions of the project and in some cases go back to previous versions if issues were discovered. 

Finally, the code was well documented and tested meaning that issues were removed and that it's easy to understand what the different parts are doing, so if other people were to take over the project after its completion, they should be able to understand what each function's purpose is. 

There are a couple of areas where the project could be improved or enhanced, firstly a different visualisation library such as plotly could be used to make the charts interactive, this may be useful for finding out more about the data and so improve the overall effectiveness of the project. Next, the ability to read in data could be extended beyond just Kaggle, which would allow for a wider range of data to be analysed. And finally, the project could be moved to a web app through a package such as dash, this would likely make it more accessible to a wider range of users than a Jupyter notebook, as it wouldn’t require any knowledge of python. 
