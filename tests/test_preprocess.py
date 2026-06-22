# Purpose: test preprocessing function for CI/CD pipeline

import pandas as pd
from src.preprocess import clean_data
import pytest


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
    
    
def test_remove_duplicates():
    import pandas as pd
    from src.preprocess import remove_duplicates

    df = pd.DataFrame({
        "customer_id": [1, 1, 2],
        "age": [25, 25, 30]
    })

    result = remove_duplicates(df)

    assert len(result) == 2
    assert result.duplicated().sum() == 0
    
import pandas as pd
from src.preprocess import validate_target_column


def test_validate_target_column_passes():
    df = pd.DataFrame({
        "churn": [1, 0, 1],
        "age": [25, 30, 40]
    })

    validate_target_column(df)  # should NOT raise error


def test_validate_target_column_fails():
    df = pd.DataFrame({
        "age": [25, 30, 40]
    })

    with pytest.raises(ValueError):
        validate_target_column(df)