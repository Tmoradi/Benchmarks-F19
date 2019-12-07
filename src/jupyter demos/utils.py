import pandas as pd

def get_series(df,original_column,target_column):
    df[target_column],court_uniques = pd.factorize(df[original_column])
    court_type_mapping={}
    for index,value in enumerate(court_uniques.values):
        court_type_mapping[index]=value
    court_type_mapping
    return df, court_type_mapping

def get_court_name_type(df):
    df,court_type_mapping=get_series(df,'Court Type','Court Type values')
    df,lower_court_mapping=get_series(df,'Lower Court','Lower Court values')
    df,judge_mapping=get_series(df,'Lower Ct Judge','Lower Court Judge values')
    return df, court_type_mapping,lower_court_mapping,judge_mapping 