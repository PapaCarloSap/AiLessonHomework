from pathlib import Path
import pandas as pd


# def test_readline():
#     from Megafon.Course_project.data_manager import DataManager
#     path_data:Path = Path(r'Megafon\Course_project\tests\data_manager_file_data.txt') 
#     path_features:Path = Path(r'Megafon\Course_project\tests\data_manager_file_features.txt') 
#     target = DataManager(path_data=path_data, path_features=path_features)
#     df:pd.DataFrame = target.get_short_data(percent=0.67)
#     assert 4 == df.shape[0]

def test_data_df():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    source_df = target.get_full_data(reload_csv = True, update_source = True)           
    assert (5, 257) == source_df.shape

def test_users_generate_source():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    data_df, features_df = target._init_data_and_features() 
    source_df = target._generate_source_data(data_df, features_df)          
    source_df, missing = target._clean_data(source_df)
    assert (3, 257) == source_df.shape
    assert (4, 257) == missing.shape

def test_external_users_generate_source():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    df:pd.DataFrame = target.get_full_data(reload_csv = True, update_source = True)
    result, missing = target.get_data_for_users(path_data)
    assert (3, 257) == result.shape

def test_users_generate_source_v2():
    from Megafon.Course_project.data_manager import DataManager
    path_data = r'Megafon\Course_project\tests\data_manager_file_data.txt'
    path_features = r'Megafon\Course_project\tests\data_manager_file_features.txt'
    target = DataManager(path_data=path_data, path_features=path_features)
    data_df, features_df = target._init_data_and_features() 
    df = target._get_forward_data_by_date(data_df[1:5], data_df, features_df)
    source_df, missing = target._clean_data(df)
    assert (3, 257) == source_df.shape