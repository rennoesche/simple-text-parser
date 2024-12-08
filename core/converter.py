from pdfminer.high_level import extract_text

def convert_pdf(file_path):
    try:
        text = extract_text(file_path)
        if text.strip():
            return text
        else:
            raise ValueError("File tidak berisi teks.")
    except Exception as e:
        raise ValueError(f"Error saat membaca file: {e}")