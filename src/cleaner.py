import pandas as pd

def clean_table(df):
    """
    Clean extracted table.
    """

    print("Cleaning table...")

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove completely empty columns
    df = df.dropna(axis=1, how="all")

    # Reset row index
    df = df.reset_index(drop=True)

    # Use first row as column names
    df.columns = df.iloc[0]

    # Remove first row (it is now the header)
    df = df[1:]

    # Reset index again
    df = df.reset_index(drop=True)

    # Remove leading/trailing spaces
    df = df.apply(lambda col: col.astype(str).str.strip())

    return df