import pdfplumber

def analyze_pdf(pdf_path):
        
    """
    Analyze a PDF and determine:
    - Number of pages
    - Whether it is digital or scanned
    """

    ##print(f"Analyzing PDF: {pdf_path}")

    with pdfplumber.open(pdf_path) as pdf:
        ##print(f"Number of pages: {len(pdf.pages)}")

        is_scanned = True

        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()

            if text and text.strip():
                is_scanned = False
                ##print(f"Page {page_number} appears to be digital (text found).")
            ##else:
                ##print(f"Page {page_number} appears to be scanned (no text found).")

        if is_scanned:
            print("\nPDF Type : Scanned PDF")
            return "scanned"

        print("\nPDF Type : Digital PDF")
        return "digital"
