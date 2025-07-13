# core/metadata_extractor.py
import os
import zipfile
from PyPDF2 import PdfReader
import docx
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    if not os.path.isfile(file_path):
        return "Invalid file path."

    ext = os.path.splitext(file_path)[1].lower()

    try:
        if ext == ".pdf":
            return extract_pdf_metadata(file_path)
        elif ext == ".docx":
            return extract_docx_metadata(file_path)
        elif ext in [".jpg", ".jpeg", ".png"]:
            return extract_image_metadata(file_path)
        elif ext == ".zip":
            return extract_zip_metadata(file_path)
        else:
            return "Unsupported file type."
    except Exception as e:
        return f"Error: {str(e)}"

def extract_pdf_metadata(path):
    reader = PdfReader(path)
    meta = reader.metadata
    return "\n".join([f"{k}: {v}" for k, v in meta.items() if v])

def extract_docx_metadata(path):
    doc = docx.Document(path)
    props = doc.core_properties
    return "\n".join([
        f"Author: {props.author}",
        f"Title: {props.title}",
        f"Created: {props.created}",
        f"Modified: {props.modified}"
    ])

def extract_image_metadata(path):
    img = Image.open(path)
    exif_data = img._getexif()
    if not exif_data:
        return "No EXIF metadata found."
    output = ""
    for tag, val in exif_data.items():
        decoded = TAGS.get(tag, tag)
        output += f"{decoded}: {val}\n"
    return output

def extract_zip_metadata(path):
    with zipfile.ZipFile(path, 'r') as zip_ref:
        info = zip_ref.infolist()
        return "\n".join([f"{f.filename} - {f.file_size} bytes" for f in info])
