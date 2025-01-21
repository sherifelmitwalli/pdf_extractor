from pdf_extractor.extractor import extract_text_hybrid, save_text_to_file
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='PDF Text Extraction Tool')
    parser.add_argument('pdf_path', help='Path to the PDF file')
    parser.add_argument('-o', '--output', default='output.json',
                       help='Output file path (default: output.json)')
    
    args = parser.parse_args()
    
    # Extract text using hybrid method
    extracted_text = extract_text_hybrid(args.pdf_path)
    
    # Save results to specified output file
    save_text_to_file(extracted_text, args.output)
    
    print(f"Extraction complete! Results saved to {args.output}")

if __name__ == '__main__':
    main()
