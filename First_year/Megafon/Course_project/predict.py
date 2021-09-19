import pickle
from sklearn.pipeline import Pipeline
import pandas as pd
import datetime

DATATEST_CSV = r'Megafon\Course_project\temp_data\data_test.csv'
FEATURES_CSV = r'Megafon\Course_project\temp_data\features.csv'
# DATATEST_CSV = 'data_test.csv'
# FEATURES_CSV = 'features.csv'

def main():
    data_df = pd.read_csv(DATATEST_CSV, sep=',').drop(columns=['Unnamed: 0'])
    data_df['buy_time_convert'] = data_df['buy_time'].transform(datetime.datetime.fromtimestamp)
    data_df = data_df.sort_values(by=['buy_time_convert'])
    #answers_df = data_df[['buy_time', 'id', 'vas_id']]
    #data_df = data_df.drop(columns='buy_time')

    features_df = pd.read_csv(FEATURES_CSV, sep='\t').drop(columns=['Unnamed: 0'])
    features_df['buy_time_convert'] = features_df['buy_time'].transform(datetime.datetime.fromtimestamp)
    features_df = features_df.sort_values(by=['buy_time_convert'])
    features_df = features_df.drop(columns='buy_time')


    source_df = pd.merge_asof(data_df, features_df, on='buy_time_convert', by='id')
    missing_features = source_df[source_df.isnull().sum(axis=1)>252]
    source_df.drop(missing_features.index), missing_features
    answers_df = source_df[['buy_time', 'id', 'vas_id']]
        
    model : Pipeline = None
    with open('temp_model_rfg.pkl', 'rb') as handle:
        model = pickle.load(handle)
        answers_df['target'] = model.predict_proba(source_df)[:,1]
        answers_df.to_csv('answers_test.csv', index=False)

if __name__ == '__main__':
    main()
