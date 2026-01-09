from pathlib import Path
from ocr.image_reader import read_image
from ocr.clean_text import clean_text

BASE_DIR = Path(__file__).resolve().parent
image_path = BASE_DIR / "samples" / "sample_report.jpg"

print("Resolved path:", image_path)
print("File exists:", image_path.exists())

text = read_image(image_path)
cleaned = clean_text(text)

print("===== OCR OUTPUT =====")
print(cleaned)
