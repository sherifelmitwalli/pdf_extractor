from pdf_extractor.extractor import PDFExtractor
import argparse

def main():
    parser = argparse.ArgumentParser(description='PDF Text Extraction Tool')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', default='output.json',
                       help='Output file path (default: output.json)')
    parser.add_argument('-f', '--format', choices=['json', 'txt'],
                       default='json', help='Output format (default: json)')
    
    args = parser.parse_args()
    
    extractor = PDFExtractor(args.pdf_path)
    extractor.process_pdf()
    extractor.save_results(args.output, args.format)
    
    print(f"Extraction complete! Results saved to {args.output}")

if __name__ == '__main__':
    main()
