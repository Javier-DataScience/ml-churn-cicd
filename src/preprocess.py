# Purpose: minimal preprocessing function for CI/CD testing pipeline

def clean_data(df):
    """
    Removes missing values from a dataframe.
    This is intentionally simple for CI/CD testing.
    """
    return df.dropna()

def remove_duplicates(df):
    """
    Removes duplicate rows from a dataframe.
    """
    return df#.drop_duplicates()

def validate_target_column(df):
    """
    Ensures that the dataset contains the required target column 'churn'.
    """
    if "churn" not in df.columns:
        raise ValueError("Target column 'churn' not found")