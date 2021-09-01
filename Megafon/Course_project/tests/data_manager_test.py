from pathlib import Path
import pandas as pd


# def test_readline():
#     from Megafon.Course_project.data_manager import DataManager
#     path_data:Path = Path(r'Megafon\Course_project\tests\data_manager_file_data.txt') 
#     path_features:Path = Path(r'Megafon\Course_project\tests\data_manager_file_features.txt') 
#     target = DataManager(path_data=path_data, path_features=path_features)
#     df:pd.DataFrame = target.get_short_data(percent=0.67)
#     assert 4 == df.shape[0]

def test_users_generate_source():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    df:pd.DataFrame = target.get_full_data(reload=True)
    assert (2, 257) == df.shape

def test_external_users_generate_source():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    df:pd.DataFrame = target.get_full_data(reload=True)
    result = target.get_data_for_users(path_data)
    assert (2, 257) == result.shape