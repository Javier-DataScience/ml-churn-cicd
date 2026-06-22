# Purpose: test preprocessing function for CI/CD pipeline

import pandas as pd
from src.preprocess import clean_data


def test_clean_data_removes_nans():
    df = pd.DataFrame({
        "a": [1, 2, None],
        "b": [4, None, 6]
    })

    result = clean_data(df)

    # Assert no missing values remain
    assert result.isnull().sum().sum() == 0

    # Assert expected row count (only rows without NaNs survive)
    assert len(result) == 1