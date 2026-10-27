"""
Script to run notebooks and convert them into html and pdf files

Steps:
1) Clean notebooks using nbstripout (can be skipped via "--no-clean")
2) Run notebooks using nbconvert and clear some metadata (can be skipped via "--no-run")
3) Export notebooks as html files (can be skipped via "--no-html")
4) Export notebooks as pdf files (can be skipped via "--no-pdf")

Usage:
cd PCP/
python tools/run_and_export_notebooks.py                           # run for all notebooks
python tools/run_and_export_notebooks.py -n PCP_04_control.ipynb   # run for single notebook

Author: Sebastian Strahl
"""

import subprocess
import sys
import argparse
import re

ALL_NOTEBOOKS = [
    "PCP.ipynb",
    "PCP_01_getstarted.ipynb",
    "PCP_02_python.ipynb",
    "PCP_03_numpy.ipynb",
    "PCP_04_control.ipynb",
    "PCP_05_vis.ipynb",
    "PCP_06_complex.ipynb",
    "PCP_07_exp.ipynb",
    "PCP_08_signal.ipynb",
    "PCP_09_dft.ipynb",
    "PCP_10_module.ipynb",
]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process Jupyter notebooks.")
    parser.add_argument("--notebook", "-n", type=str, help="Specify a notebook to process (if not specified: process all notebooks)")
    parser.add_argument("--no-clean", dest="clean", action="store_false", help="Skip cleaning the notebooks using nbstripout")
    parser.add_argument("--no-run", dest="run", action="store_false", help="Skip running the notebooks")
    parser.add_argument("--no-html", dest="html", action="store_false", help="Skip the html export of the notebooks")
    parser.add_argument("--no-pdf", dest="pdf", action="store_false", help="Skip the pdf export of the notebooks")
    parser.add_argument("--strict", action="store_true", help="Abort with an error (instead of a warning) if a pdf export has fallback fonts")
    args = parser.parse_args()

    if args.notebook:
        notebooks = [args.notebook]
    else:
        notebooks = ALL_NOTEBOOKS

    failed_pdfs = []
    for nb in notebooks:
        print(f"Processing {nb}...")

        try:
            if args.clean:
                # Strip outputs & metadata first
                subprocess.run(["nbstripout", nb], check=True)

            if args.run:
                # Execute notebook in-place
                subprocess.run(
                    ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "--ClearMetadataPreprocessor.enabled=True", nb],
                    check=True,
                )

            if args.html:
                # Convert notebook to html
                subprocess.run(
                    ["jupyter", "nbconvert", "--to", "html", "--template", "classic", "--config", "tools/nbconvert_config.py", nb],
                    check=True,
                )

            if args.pdf:
                # Convert notebook to pdf
                subprocess.run(
                    ["jupyter", "nbconvert", "--to", "webpdf", "--template", "lab_custom", "--TemplateExporter.extra_template_basedirs", "./tools", "--config", "tools/nbconvert_config.py", nb],
                    check=True,
                )

                # Check whether math was rendered with fallback fonts (MathJax fonts not loaded in time).
                # Then math variables use an italic system font (e.g., Tinos-Italic) instead of MathJax fonts.
                pdf_file = nb.replace(".ipynb", ".pdf")
                with open(pdf_file, "rb") as f:
                    if re.search(rb"/BaseFont\s*/[A-Z]{6}\+(?!Constantia)[\w-]*Italic", f.read()):
                        failed_pdfs.append(nb)

        # Immediately stop if processing fails for one notebook
        except subprocess.CalledProcessError:
            print(f"Processing failed for {nb}")
            sys.exit(1)

    # Report failed pdf exports at the end so that the warning does not get lost in the nbconvert output
    for nb in failed_pdfs:
        print(f"WARNING: PDF export failed for {nb} (math rendered with fallback fonts). Simply try again:")
        print(f"python tools/run_and_export_notebooks.py -n {nb} --no-clean --no-run --no-html")
    if failed_pdfs and args.strict:
        sys.exit(1)
