import os

from detector import analyze_pdf
from extractor import extract_tables
from cleaner import clean_table
from exporter import export_csv
from exporter import export_json
from merger import merge_tables
from ocr import extract_text_from_scanned_pdf
from logger import logger
from chunker import chunk_tables

INPUT_FOLDER = "input"

print("=" * 60)
print("TABLE EXTRACTION PROJECT")
print("=" * 60)


def process_document(pdf_path, filename):
    """
    Complete pipeline for one PDF.
    """

    print("\n" + "=" * 60)
    print(f"Processing : {filename}")
    print("=" * 60)

    # Step 1: Analyze PDF
    pdf_type = analyze_pdf(pdf_path)
    logger.info(f"{filename} detected as {pdf_type} PDF")

    # If the PDF is scanned, use OCR
    if pdf_type == "scanned":

        print("\nScanned PDF detected.")

        ocr_df = extract_text_from_scanned_pdf(pdf_path)

        print("\nOCR Output:")
        print(ocr_df)

        # Stop further processing for now
        return

    # Step 2: Extract tables
    tables = extract_tables(pdf_path)
    logger.info(f"{len(tables)} tables extracted")

    # If no tables found, skip the document
    if not tables:
        print("No tables found.")
        return

    # Remove ".pdf" from filename
    document_name = os.path.splitext(filename)[0]

    # Create output folder for this document
    output_folder = os.path.join("output", document_name)

    # Store all cleaned tables for JSON export
    cleaned_tables = []

    # Step 3: Clean and Export
    for table_number, table in enumerate(tables, start=1):

        print(f"\nCleaning Table {table_number}")

        cleaned_df = clean_table(table)

        logger.info(
            f"Table {table_number} cleaned"
        )

        cleaned_tables.append(cleaned_df)

    # Merge continuation tables
    cleaned_tables = merge_tables(cleaned_tables)

    chunks = chunk_tables(
        cleaned_tables,
        chunk_size=20
    )

    print(f"\nGenerated {len(chunks)} chunks.")

    for chunk in chunks:

        print("=" * 60)

        print(
            f"Table {chunk['table']} "
            f"Chunk {chunk['chunk']}"
        )

        print(chunk["data"])

    logger.info(
        f"{len(cleaned_tables)} tables after merging"
    )

    # Export merged tables
    for table_number, table in enumerate(cleaned_tables, start=1):

        export_csv(
            table,
            output_folder,
            table_number
        )

        logger.info(
            f"Table {table_number} exported to CSV"
        )

    export_json(
        document_name,
        cleaned_tables,
        output_folder
    )

    logger.info(
        f"All tables exported to JSON"
    )

def main():

    if not os.path.exists(INPUT_FOLDER):
        print(f"Input folder '{INPUT_FOLDER}' not found.")
        return

    files = os.listdir(INPUT_FOLDER)

    if not files:
        print("No PDF files found.")
        return

    for file in files:

        if file.lower().endswith(".pdf"):

            pdf_path = os.path.join(INPUT_FOLDER, file)

            process_document(pdf_path, file)


if __name__ == "__main__":
    main()