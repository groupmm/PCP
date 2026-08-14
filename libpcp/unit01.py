"""
Module: libpcp.unit01
Author: Meinard Mueller, International Audio Laboratories Erlangen
License: The MIT license, https://opensource.org/licenses/MIT
This file is part of the PCP Notebooks (https://www.audiolabs-erlangen.de/PCP)
"""

from pathlib import Path

def print_zip_url():
    """
    Prints the URL of the current version's zip file.
    """
    __version__ = Path("VERSION").read_text().strip()
    url = f"https://github.com/groupmm/PCP/releases/download/v{__version__}/PCPT_{__version__}.zip"
    border = "-" * (len(url))
    print(border)
    print(url)
    print(border)
    