import re


def clean_text(text: str) -> str:
    """
    Clean and normalize OCR extracted text.
    """

    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)

    # Remove non-ASCII characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # Strip leading/trailing spaces
    return text.strip()
