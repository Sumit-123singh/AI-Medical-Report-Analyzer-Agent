from pdf2image import convert_from_path
from pathlib import Path
import pytesseract
import cv2
import numpy as np
from PIL import Image


# =========================
# CONFIGURATION
# =========================

# Poppler path (Windows)
POPPLER_PATH = r"C:\poppler\Library\bin"

SUPPORTED_IMAGE_FORMATS = {".png", ".jpg", ".jpeg"}
SUPPORTED_PDF_FORMATS = {".pdf"}


# =========================
# HELPER FUNCTION
# =========================

def _ocr_image(image: np.ndarray) -> str:
    """Preprocess and OCR a single image"""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 3)
    gray = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return pytesseract.image_to_string(gray, lang="eng")


# =========================
# MAIN FUNCTION
# =========================

def read_pdf(file_path: str | Path) -> str:
    """
    Extract text from PDF, PNG, JPG, JPEG using OCR.
    (Function name kept same to avoid breaking imports)
    """

    file_path = Path(file_path)

    # Validate file
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = file_path.suffix.lower()
    extracted_text = []

    # =========================
    # PDF HANDLING
    # =========================
    if suffix in SUPPORTED_PDF_FORMATS:
        try:
            pages = convert_from_path(
                str(file_path),
                dpi=300,
                poppler_path=POPPLER_PATH
            )
        except Exception as e:
            raise RuntimeError(
                "Failed to convert PDF to images. "
                "Ensure Poppler is installed and path is correct."
            ) from e

        for page_number, page in enumerate(pages, start=1):
            image = np.array(page)
            text = _ocr_image(image)
            extracted_text.append(f"\n--- Page {page_number} ---\n{text}")

    # =========================
    # IMAGE HANDLING
    # =========================
    elif suffix in SUPPORTED_IMAGE_FORMATS:
        try:
            image = Image.open(file_path)
            image = np.array(image)
            text = _ocr_image(image)
            extracted_text.append(text)
        except Exception as e:
            raise RuntimeError("Image OCR failed.") from e

    else:
        raise ValueError(
            f"Unsupported file format: {suffix}. "
            "Allowed: PDF, PNG, JPG, JPEG"
        )

    return "\n".join(extracted_text)
