import pytesseract
from pdf2image import convert_from_path
import pandas as pd


def extract_text_from_scanned_pdf(pdf_path):

    print("Running OCR...")

    images = convert_from_path(pdf_path)

    rows = []

    for page_number, image in enumerate(images, start=1):

        text = pytesseract.image_to_string(image)

        rows.append({

            "page": page_number,

            "text": text

        })

    return pd.DataFrame(rows)