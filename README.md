# LaTeX Compiler

A lightweight Python script to batch-compile `.tex` files into PDFs using `pdflatex`.

## 📂 Folder Structure

- `batch/` — place your `.tex` files here
- `output/` — compiled PDFs will be saved here
- `old/` — processed `.tex` files are moved here after compilation

## ▶️ Usage

Make sure you have `pdflatex` installed (comes with most LaTeX distributions like TeX Live or MiKTeX).

Then run:

```bash
python Compiler.py
