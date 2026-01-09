from pathlib import Path
import cv2
import pytesseract

# 🔴 HARD-CODE TESSERACT PATH (WINDOWS FIX)
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def read_image(image_path: Path) -> str:
    """
    Extract text from an image using OCR.
    """

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)

    if image is None:
        raise ValueError("OpenCV could not read image")

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize to improve OCR accuracy
    gray = cv2.resize(
        gray, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC
    )

    # Thresholding
    gray = cv2.threshold(
        gray, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    # OCR
    text = pytesseract.image_to_string(gray)

    return text
