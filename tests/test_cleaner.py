import pandas as pd

from src.cleaner import clean_table


def test_clean_table():

    df = pd.DataFrame([

        ["Name", "Age"],

        ["John", 25],

        ["Alice", 30]

    ])

    cleaned = clean_table(df)

    assert list(cleaned.columns) == ["Name", "Age"]

    assert len(cleaned) == 2