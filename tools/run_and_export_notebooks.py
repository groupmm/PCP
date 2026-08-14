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
    args = parser.parse_args()

    if args.notebook:
        notebooks = [args.notebook]
    else:
        notebooks = ALL_NOTEBOOKS

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

        # Immediately stop if processing fails for one notebook
        except subprocess.CalledProcessError:
            print(f"Processing failed for {nb}")
            sys.exit(1)
