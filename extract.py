import fitz 
from cleanup import cleanup

SECTION_TITLES = [
    "Introduction",  
    "INTRODUCTION",  
    "Contents"
]

def extract_text(pdf_path):
    """Extract text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

def extract_abstract(pdf_text):
    """Extract content from the PDF text up to, but excluding, the first matched section title."""
    earliest_start_idx = float('inf')
    matched_title = None
    
    for title in SECTION_TITLES:
        idx = pdf_text.find(title)
        if idx != -1 and idx < earliest_start_idx:
            earliest_start_idx = idx
            matched_title = title
    
    if matched_title:
        return pdf_text[:earliest_start_idx].strip()
    else:
        return "Content not found"



def extract(pdf_path):
    pdf_text = extract_text(pdf_path)
    content = extract_abstract(pdf_text, SECTION_TITLES)
    # print(f"{content}\n")
    
    return content
