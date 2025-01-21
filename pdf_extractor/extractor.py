import json
import os
import logging
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

def extract_text_hybrid(pdf_path):
    """Extract text using hybrid PyPDF2 + Tesseract OCR approach"""
    results = {}
    reader = PdfReader(pdf_path)
    
    for i, page in enumerate(reader.pages):
        try:
            # First try PyPDF2 text extraction
            text = page.extract_text()
            
            # If PyPDF2 returns empty or very short text, use OCR
            if not text or len(text.strip()) < 100:
                logging.info(f"Using OCR for page {i+1}")
                images = convert_from_path(pdf_path, first_page=i+1, last_page=i+1)
                text = pytesseract.image_to_string(images[0], lang='eng')
            
            results[f"page_{i+1}"] = text
            logging.info(f"Processed page {i+1}")
            
        except Exception as e:
            logging.error(f"Error processing page {i+1}: {str(e)}")
            results[f"page_{i+1}"] = f"Error: {str(e)}"
    
    return results

def get_page_count(pdf_path):
    """Get total number of pages in PDF"""
    return len(PdfReader(pdf_path).pages)

def convert_pdf_page_to_image(pdf_path, page_num):
    """Convert PDF page to image using pdf2image"""
    images = convert_from_path(pdf_path, first_page=page_num+1, last_page=page_num+1)
    return images[0]

def save_text_to_file(text, output_path):
    """Save extracted text to JSON file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(text, f, indent=4, ensure_ascii=False)

def list_pdf_files():
    """List all PDF files in current directory"""
    pdf_files = [f for f in os.listdir() if f.lower().endswith('.pdf')]
    if not pdf_files:
        print("No PDF files found in current directory.")
        return None
    
    print("Available PDF files:")
    for i, f in enumerate(pdf_files, 1):
        print(f"{i}. {f}")
    
    while True:
        try:
            choice = int(input("Enter the number of the PDF to process: "))
            if 1 <= choice <= len(pdf_files):
                return pdf_files[choice - 1]
            print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Get PDF file to process
    pdf_file = list_pdf_files()
    if not pdf_file:
        exit(1)
        
    # Use PDF filename (without extension) for output JSON
    pdf_name = os.path.splitext(os.path.basename(pdf_file))[0]
    output_path = os.path.join(os.getcwd(), f"{pdf_name}_extracted.json")
    
    logging.info("Starting hybrid text extraction...")
    extracted_text = extract_text_hybrid(pdf_file)
    save_text_to_file(extracted_text, output_path)
    logging.info(f"Text extraction complete! Saved to {output_path}")
