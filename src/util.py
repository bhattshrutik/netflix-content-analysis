import pandas as pd

def load_data(path="data/netflix_titles.csv"):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['year_added'] = df['date_added'].dt.year
    df['month_added'] = df['date_added'].dt.month
    df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype('Int64')
    df['listed_in'] = df['listed_in'].fillna('')
    df['listed_in'] = df['listed_in'].apply(lambda x: [i.strip() for i in x.split(',')])
    df['country'] = df['country'].fillna('')
    df['country'] = df['country'].apply(lambda x: [i.strip() for i in x.split(',')])
    return df
