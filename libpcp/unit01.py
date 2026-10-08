"""
Module: libpcp.unit01
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

from pathlib import Path


def print_zip_url():
    """Print the URL of the ZIP archive for the current PCP version.

    Notebook: PCP_01_getstarted.ipynb
    """
    version = Path('VERSION').read_text().strip()
    url = f'https://github.com/groupmm/PCP/releases/download/v{version}/PCP_{version}.zip'
    border = '-' * len(url)
    print(border)
    print(url)
    print(border)
