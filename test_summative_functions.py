import pytest

from summative_functions import *

@pytest.fixture
def get_data():
    test_data = pd.read_csv("/work/owain_summative/test_data", index_col=0)
    return test_data

@pytest.fixture
def set_new_cols():
    new_cols = ["Products SKU", "Bank", "Mortgage product subtitle", 
    "Product type subtitle", "Product type", "Length of Mortgage", 
    "Initial Rate","APR percentage", "Revert Rate", "Total Fees", "Initial Rate months", "Date scanned","ID KEY"]

    return new_cols


def test_import_data():
    assert import_data(43) == None
    assert import_data("https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource") == None


def test_get_folder_name():
    assert get_folder_name("https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog") == 'usedcarscatalog'
    assert get_folder_name("https://www.kaggle.com/datasets/camnugent/california-housing-prices") == 'california-housing-prices'


def test_clean_col_names(get_data, set_new_cols):
    assert clean_col_names("get_data", set_new_cols) == None
    assert clean_col_names(get_data, "set_new_cols") == None
    assert clean_col_names(get_data, {3:4,4:3}) == None
    assert clean_col_names(get_data, [1,2,3,4]) == None
    assert clean_col_names(get_data, ["Products SKU", "Bank", "Mortgage product subtitle", 
    "Product type subtitle", "Product type", "Length of Mortgage"]) == None

    joined_dict = dict(zip(get_data.columns, set_new_cols))
    renamed_df = get_data.rename(columns = joined_dict)
    assert clean_col_names(get_data,set_new_cols).equals(renamed_df)
