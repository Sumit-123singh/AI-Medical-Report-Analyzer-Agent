from pdf2image import convert_from_path
from pathlib import Path
import pytesseract
import cv2
import numpy as np


def read_pdf(pdf_path: Path) -> str:
    """
    Extract text from a scanned PDF using OCR.
    """

    # Convert PDF pages to images
    pages = convert_from_path(str(pdf_path))

    extracted_text = ""

    for page in pages:
        # Convert PIL image to OpenCV format
        image = np.array(page)

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to improve OCR accuracy
        gray = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # Perform OCR on the page
        text = pytesseract.image_to_string(gray)

        extracted_text += text + "\n"

    return extracted_text
