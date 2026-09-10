#!/usr/bin/env bash
# Build the merged PCP pdf booklet: tools/pdf_booklet/PCP_all.pdf
# Usage: tools/build_booklet.sh

set -e  # stop on the first error

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"

# Activate conda environment
eval "$(conda shell.bash hook)"
conda activate PCP

# Run the notebooks and export them as html/pdf files (from the repo root)
echo "==> Running and exporting notebooks"
cd "$REPO_DIR"
python tools/run_and_export_notebooks.py

# Extract annotations of the exported pdf files, so that hyperlinks survive the merge
echo "==> Extracting pdf annotations"
cd "$REPO_DIR/tools/pdf_booklet"
texlua extract_annotations.lua

# Compile twice for correct table of contents and page numbers
for pass in 1 2; do
    echo "==> Compiling PCP_all.tex (pass $pass)"
    xelatex -interaction=nonstopmode -halt-on-error PCP_all.tex > /dev/null
done

echo "==> Done: tools/pdf_booklet/PCP_all.pdf"
