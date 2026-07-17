import camelot
import pdfplumber
import pandas as pd


def extract_tables(pdf_path):
    """
    Hybrid table extraction:
    1. Camelot Lattice
    2. Camelot Stream
    3. pdfplumber
    """

    print(f"\nExtracting tables from: {pdf_path}")

    # ---------- Try Camelot Lattice ----------
    try:
        print("Trying Camelot Lattice...")

        tables = camelot.read_pdf(
            pdf_path,
            pages="all",
            flavor="lattice"
        )

        if tables.n > 0:
            print(f"✓ Lattice found {tables.n} table(s)")
            return [table.df for table in tables]

    except Exception as e:
        print("Lattice failed:", e)

    # ---------- Try Camelot Stream ----------
    try:
        print("Trying Camelot Stream...")

        tables = camelot.read_pdf(
            pdf_path,
            pages="all",
            flavor="stream"
        )

        if tables.n > 0:
            print(f"✓ Stream found {tables.n} table(s)")
            return [table.df for table in tables]

    except Exception as e:
        print("Stream failed:", e)

    # ---------- Try pdfplumber ----------
    print("Trying pdfplumber...")

    extracted_tables = []

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            tables = page.extract_tables()

            for table in tables:

                df = pd.DataFrame(table)

                extracted_tables.append(df)

    if extracted_tables:
        print(f"✓ pdfplumber found {len(extracted_tables)} table(s)")
        return extracted_tables

    print("No tables found.")

    return []