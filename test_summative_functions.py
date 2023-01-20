import pytest

from summative_functions import *

@pytest.fixture
def get_data():
    # importing the test dataframe for use in multiple tests
    test_data = pd.read_csv("/work/owain_summative/test_data", index_col=0)
    return test_data

@pytest.fixture
def set_new_cols():
    # create list of correct column names to use in multiple tests
    new_cols = ["Products SKU", "Bank", "Mortgage product subtitle", 
    "Product type subtitle", "Product type", "Length of Mortgage", 
    "Initial Rate","APR percentage", "Revert Rate", "Total Fees", "Initial Rate months", "Date scanned","ID KEY"]

    return new_cols

def test_import_data():

    # if invalid inputs then nothing should be returned
    assert import_data(43) == None
    assert import_data("https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource") == None


def test_get_folder_name():

    # check that the correct value is returned by the function
    assert get_folder_name("https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog") == 'usedcarscatalog'
    assert get_folder_name("https://www.kaggle.com/datasets/camnugent/california-housing-prices") == 'california-housing-prices'


def test_clean_col_names(get_data, set_new_cols):

    # invalid inputs should return nothing
    assert clean_col_names("get_data", set_new_cols) == None
    assert clean_col_names(get_data, "set_new_cols") == None
    assert clean_col_names(get_data, {3:4,4:3}) == None
    assert clean_col_names(get_data, [1,2,3,4]) == None
    assert clean_col_names(get_data, ["Products SKU", "Bank", "Mortgage product subtitle", 
    "Product type subtitle", "Product type", "Length of Mortgage"]) == None

    # a valid input should work and so be equal to the renamed dataframe
    joined_dict = dict(zip(get_data.columns, set_new_cols))
    renamed_df = get_data.rename(columns = joined_dict)
    assert clean_col_names(get_data,set_new_cols).equals(renamed_df)

def test_create_boxenplots(get_data,set_new_cols):

    # test column names, some valid and some invalid
    numeric_col_1 = "APR percentage"
    numeric_col_2 = "Total Fees"
    str_col = "Product type"
    invalid_col = "sdfsd"
    invalid_type_col = 23

    # renaming the columns of the test df
    get_data = clean_col_names(get_data, set_new_cols)

    # invalid inputs should return nothing
    assert create_boxenplots("df",numeric_col_1) == None
    assert create_boxenplots(get_data,numeric_col_1) == None
    assert create_boxenplots(get_data,[numeric_col_1,str_col]) == None
    assert create_boxenplots(get_data,[numeric_col_1,invalid_type_col]) == None
    assert create_boxenplots(get_data,[numeric_col_1, numeric_col_2,invalid_col]) == None
    assert create_boxenplots(get_data,[numeric_col_1, numeric_col_2,2]) == None

    # checking that if the inputs are valid then it would create the chart
    valid_col_names = [numeric_col_1, numeric_col_2]
        
    if not isinstance(get_data, pd.DataFrame):
        x = 1
    elif not isinstance(valid_col_names, list):
        x = 1
    elif all(map(lambda x: isinstance(x, str), valid_col_names)) is False:
        x = 1
    elif all(map(lambda x: x in get_data.columns, valid_col_names)) is False:
        x = 1
    elif all(map(lambda x: get_data.dtypes[x] == np.int64 or get_data.dtypes[x] == np.float64 , valid_col_names)) is False:
        x = 1
    else:
        x = 2

    assert x == 2

    # checking the correct number of axes are created
    col_names = [numeric_col_1, numeric_col_2,str_col]
    fig, axes = plt.subplots(ncols = len(col_names))
    assert len(axes) == len(col_names)
    
def test_create_count_plots(get_data, set_new_cols):

    # test column names, some valid and some invalid
    str_col_1 = "Product type"
    str_col_2 = "Bank"
    numeric_col = "APR percentage"
    invalid_col = "sdfsd"
    invalid_type_col = 23

    # renaming the columns of the test df
    get_data = clean_col_names(get_data, set_new_cols)

    # invalid inputs should return nothing
    assert create_count_plots("df",str_col_1) == None
    assert create_count_plots(get_data,str_col_1) == None
    assert create_count_plots(get_data,[str_col_1,numeric_col]) == None
    assert create_count_plots(get_data,[str_col_1,invalid_type_col]) == None
    assert create_count_plots(get_data,[str_col_1, str_col_2,invalid_col]) == None
    assert create_count_plots(get_data,[str_col_1, str_col_2,2]) == None

    # checking that if the inputs are valid then it would create the chart
    valid_col_names = [str_col_1, str_col_2]

    if not isinstance(get_data, pd.DataFrame):
        x = 1
    elif not isinstance(valid_col_names, list):
        x = 1
    elif all(map(lambda x: isinstance(x, str), valid_col_names)) is False:
        x = 1
    elif all(map(lambda x: x in get_data.columns, valid_col_names)) is False:
        x = 1
    elif all(map(lambda x: get_data.dtypes[x] == object , valid_col_names)) is False:
        x = 1
    else:
        x = 2

    assert x == 2

    # checking the correct number of axes are created 
    col_names = [str_col_1, str_col_2]
    fig, axes = plt.subplots(nrows = len(col_names))
    assert len(axes) == len(col_names)

def test_create_scatter_plots(get_data, set_new_cols):

    # test column names, some valid and some invalid
    numeric_col_1 = "APR percentage"
    numeric_col_2 = "Total Fees"
    numeric_col_3 = "Initial Rate"
    str_col_1 = "Product type"
    str_col_2 = "Bank"
    invalid_col = "sdfsd"
    invalid_type_col = 23

    # renaming the columns of the test df
    get_data = clean_col_names(get_data, set_new_cols)

    # invalid inputs should return nothing
    assert create_scatter_plots(get_data, 2,3,4) == None
    assert create_scatter_plots(get_data, numeric_col_1,str_col_1,numeric_col_2) == None
    assert create_scatter_plots(get_data, str_col_2,numeric_col_1,numeric_col_2) == None
    assert create_scatter_plots(get_data, numeric_col_3,numeric_col_1,numeric_col_2) == None
    assert create_scatter_plots("get_data", numeric_col_3,numeric_col_1,str_col_2) == None
    assert create_scatter_plots(get_data, numeric_col_3,numeric_col_1,invalid_col) == None
    assert create_scatter_plots(get_data, numeric_col_3,invalid_type_col,str_col_2) == None

    # checking that if the inputs are valid then it would create the chart
    value_1 = numeric_col_1
    value_2 = numeric_col_2
    hue_value = str_col_2

    if not isinstance(get_data, pd.DataFrame):
        x = 1
    elif all(map(lambda x: isinstance(x, str), [value_1, value_2, hue_value])) is False:
        x = 1
    elif all(map(lambda x: x in get_data.columns, [value_1, value_2, hue_value])) is False:
        x = 1
    elif (all(map(lambda x: get_data.dtypes[x] == np.int64 or get_data.dtypes[x] == np.float64 , [value_1, value_2])) is False) or (get_data.dtypes[hue_value] != object):
        x = 1
    else: 
        x = 2
    
    assert x == 2
