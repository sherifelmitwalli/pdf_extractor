# PDF Text Extractor

A hybrid PDF text extraction tool using PyPDF2 and Tesseract OCR.

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
- Windows: Use the included tesseract-installer.exe or download from https://github.com/tesseract-ocr/tesseract
- macOS: `brew install tesseract`
- Linux: `sudo apt install tesseract-ocr`

3. Configure Tesseract path:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example
```

## Configuration

After installation, verify Tesseract is properly configured by running:
```bash
tesseract --version
```

If the command is not found, add Tesseract to your system PATH:
- Windows: Add `C:\Program Files\Tesseract-OCR` to your system PATH
- macOS/Linux: Ensure Tesseract is in your $PATH

## Usage
You can run the extractor in two ways:

1. Using the main interface:
```bash
python main.py input.pdf
```

2. Directly using the extractor module:
```bash
python -m pdf_extractor.extractor input.pdf
```

Output will be saved to output.json by default.

## Troubleshooting

If you encounter OCR-related errors:
1. Verify Tesseract installation
2. Check the configured path in extractor.py matches your Tesseract installation
3. Ensure the Tesseract language data files are installed

