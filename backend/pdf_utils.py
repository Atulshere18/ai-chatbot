def extract_text_chunks(pdf_path, chunk_size=500):
    import fitz  # PyMuPDF

    doc = fitz.open(pdf_path)
    chunks = []

    for page in doc:
        text = page.get_text().replace('\n', ' ').strip()
        if not text:
            continue

        # Split the page's text into manageable chunks
        for i in range(0, len(text), chunk_size):
            chunk = text[i:i+chunk_size].strip()
            if chunk:
                chunks.append(chunk)

    return chunks
