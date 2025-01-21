# PDF Text Extractor

A hybrid PDF text extraction tool using PyPDF2 and Tesseract OCR.

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
- Windows: Download installer from https://github.com/tesseract-ocr/tesseract
- macOS: `brew install tesseract`
- Linux: `sudo apt install tesseract-ocr`

3. Configure Tesseract path:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example
```

## Usage
```bash
python main.py input.pdf
```

Output will be saved to output.json by default.
