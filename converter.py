import argparse
import os
from fpdf import FPDF
from docx import Document


def text_to_pdf(input_path: str, output_path: str) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            pdf.multi_cell(0, 10, line.rstrip())
    pdf.output(output_path)


def docx_to_pdf(input_path: str, output_path: str) -> None:
    doc = Document(input_path)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            pdf.multi_cell(0, 10, text)
    pdf.output(output_path)


def convert(input_path: str, output_path: str) -> None:
    ext = os.path.splitext(input_path)[1].lower()
    if ext in {".txt", ".text"}:
        text_to_pdf(input_path, output_path)
    elif ext == ".docx":
        docx_to_pdf(input_path, output_path)
    else:
        raise ValueError("Unsupported input format: {}".format(ext))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert text or Word files to PDF")
    parser.add_argument("input", help="Path to input .txt or .docx file")
    parser.add_argument("output", help="Path to output .pdf file")
    args = parser.parse_args()
    convert(args.input, args.output)


if __name__ == "__main__":
    main()
