# PDF to Image Extractor

A lightweight Python utility that extracts all embedded images from PDF files. This script processes PDFs in batch, preserving the original image quality and organizing outputs by document and page number.

## ✨ Features

- **Batch Processing**: Automatically scans a directory for all `.pdf` files.
- **Original Quality**: Extracts raw embedded images without re-compression or quality loss.
- **Smart Organization**: Creates a separate folder for each PDF inside a `results` directory.
- **Descriptive Naming**: Files are named automatically: `{pdf_name}_p{page}_{index}.{ext}`.
- **Console Feedback**: Displays extraction counts for each file upon completion.

## 📦 Requirements

- Python 3.6+
- **PyMuPDF** library

### Installation

Install the required dependency via pip:

### Install
pip install PyMuPDF

### Usage
python pdf2image.py
