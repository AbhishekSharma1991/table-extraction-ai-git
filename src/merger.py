import pandas as pd


def merge_tables(tables):
    """
    Merge tables having identical columns.
    """

    if not tables:
        return []

    merged_tables = []

    current_table = tables[0]

    for next_table in tables[1:]:

        if list(current_table.columns) == list(next_table.columns):

            print("Merging continuation table...")

            current_table = pd.concat(
                [current_table, next_table],
                ignore_index=True
            )

        else:

            merged_tables.append(current_table)

            current_table = next_table

    merged_tables.append(current_table)

    return merged_tables