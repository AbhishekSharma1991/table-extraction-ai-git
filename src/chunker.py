import pandas as pd


def chunk_table(df, chunk_size=20):
    """
    Split one dataframe into multiple chunks.
    """

    chunks = []

    total_rows = len(df)

    for start in range(0, total_rows, chunk_size):

        end = start + chunk_size

        chunk = df.iloc[start:end].copy()

        chunks.append(chunk)

    return chunks


def chunk_tables(tables, chunk_size=20):
    """
    Chunk every extracted table.
    """

    all_chunks = []

    for table_number, table in enumerate(tables, start=1):

        chunks = chunk_table(table, chunk_size)

        for chunk_number, chunk in enumerate(chunks, start=1):

            all_chunks.append({
                "table": table_number,
                "chunk": chunk_number,
                "data": chunk
            })

    return all_chunks