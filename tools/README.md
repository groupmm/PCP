# 1. Exporting the PCP Notebooks to HTML and PDF

Run the following command from the top level of this repository:

```bash
conda activate PCP
python tools/run_and_export_notebooks.py
```

This performs the following steps:
1. Clean notebooks using `nbstripout`
2. Run notebooks using `nbconvert`
3. Export notebooks as html files
4. Export notebooks as pdf files

# 2. PDF Booklet Creation

Compile `tools/pdf_booklet/PCP_all.tex` to create a single, merged PDF file that includes all PCP notebooks, along with a title page and a table of contents. This requires the exported PDF files obtained as described above. The merged booklet provides a convenient way to browse and print the entire course material. You can compile it using, e.g., `pdflatex`. Multiple compilation passes may be needed to correctly generate the table of contents and page numbers.

# 3. How to Create a New Release

1. Change contents.

2. Increase version number in [VERSION](../VERSION). No other version number changes in the source code are required.

3. Clean and run notebooks as described in [Section 1](#1-exporting-the-pcp-notebooks-to-html-and-pdf). Since the exported html and pdf files are not version-controlled, you can also skip the exports directly:

    ```bash
    python tools/run_and_export_notebooks.py --no-html --no-pdf
    ```

4. Commit changes:
    
    ```bash
    git add .
    git commit -m "<description of changes>"
    git push
    ```

5. Create and push tag (same number as in [VERSION](../VERSION)):
    
    ```bash
    git tag v0.0.0
    git push origin v0.0.0
    ```

    Upon this action, a GitHub runner automatically does the following steps (as configured in [build_and_release.yaml](../.github/workflows/build_and_release.yaml), takes about 5 minutes):

    1. Export all notebooks as html and pdf files using `tools/run_and_export_notebooks.py`.
    2. Create the merged pdf booklet using `tools/pdf_booklet/PCP_all.tex`.
    3. Create a zip file of the repository contents as well as the exported html and pdf files and upload it as a release asset. This zip file is then accessible via such a link with the corresponding version number:<br> 
    [https://github.com/groupmm/PCP/releases/download/v0.0.0/PCP_0.0.0.zip](https://github.com/groupmm/PCP/releases/download/v0.0.0/PCP_0.0.0.zip)

6. Edit release notes on GitHub.