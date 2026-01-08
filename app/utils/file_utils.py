from fastapi import UploadFile
from pathlib import Path
import shutil
import uuid

ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png"}


def save_uploaded_file(file: UploadFile, upload_dir: Path) -> Path:
    """
    Save uploaded file to disk safely and return file path.
    """

    upload_dir.mkdir(exist_ok=True)

    file_ext = Path(file.filename).suffix.lower()

    if file_ext not in ALLOWED_EXTENSIONS:
        raise ValueError("Unsupported file type")

    safe_filename = f"{uuid.uuid4()}{file_ext}"
    file_path = upload_dir / safe_filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
