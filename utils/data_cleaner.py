def clean_data(df):

    duplicates = df.duplicated().sum()

    missing = df.isnull().sum().sum()

    df = df.drop_duplicates()

    return df, duplicates, missing