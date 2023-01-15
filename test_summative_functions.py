# import pytest

# from summative_functions import *



# def test_import_data():
#     assert import_data(43) == "Invalid input, file path must be a string"
#     assert import_data("https://github.com/microsoft/pyright/blob/main/docs/configuration.md#reportMissingModuleSource") == "You must enter a url to a dataset within kaggle"


import os
print("PYTHONPATH:", os.environ.get('PYTHONPATH'))
print("PATH:", os.environ.get('PATH'))