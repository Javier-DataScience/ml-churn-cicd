# Purpose: minimal preprocessing function for CI/CD testing pipeline

def clean_data(df):
    """
    Removes missing values from a dataframe.
    This is intentionally simple for CI/CD testing.
    """
    return df.dropna()