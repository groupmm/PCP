# Preparation Course Python Notebooks

The Preparation Course in Python (PCP) is an open-source course in scientific programming built around ten Jupyter notebooks. The opening units cover the working environment, Python, NumPy, control structures, functions, and visualization. The later units apply these tools to complex numbers, exponential functions, signals, sampling, the discrete Fourier transform (DFT), and the fast Fourier transform (FFT). A final unit introduces modules and packages for organizing reusable code. This repository contains the PCP notebooks together with the required data and the Python package `libpcp`. No advanced programming knowledge is required. The PCP notebooks are not intended as a comprehensive introduction to Python; for this, we refer to online sources such as [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) or the [Scientific Python Lectures](https://lectures.scientific-python.org/). We use the notebooks in programming and laboratory courses for FAU study programmes such as [Communications and Multimedia Engineering (CME)](https://www.cme.studium.fau.de/), [Electrical Engineering (EEI)](https://www.eei.studium.fau.de/), [Information and Communication Technology (ICT)](https://www.iuk.studium.fau.eu/), [Data Science](https://www.datascience.nat.fau.eu/), and [Artificial Intelligence (AI)](https://www.aibe.tf.fau.de/). They also provide a foundation for the [Preparation Course in PyTorch (PCPT)](https://github.com/groupmm/PCPT) and the [Fundamentals of Music Processing (FMP)](https://www.audiolabs-erlangen.de/FMP) notebooks. The PCP Notebooks are freely accessible under the [MIT License](https://opensource.org/licenses/MIT).

If a static view of the PCP notebooks is enough for you, the [exported HTML versions](https://www.audiolabs-erlangen.de/PCP) can be used right away without any installation. All material including the explanations, the figures, and the audio examples can be accessed by just following the **HTML links**. If you want to **execute** the Python code cells, you have to download the notebooks along with the data (as the [ZIP archive of the latest release](https://github.com/groupmm/PCP/releases/latest), which also contains the exported HTML files, or by cloning this repository), create an environment, and start a Jupyter server. You then need to follow the **IPYNB links** within the Jupyter session. The necessary steps are explained in detail in the [PCP notebook on how to get started](https://www.audiolabs-erlangen.de/resources/MIR/PCP/PCP_01_getstarted.html).

## Reference

If you use the PCP Notebooks in your teaching or research, please consider the following reference.

```bibtex
@article{MuellerR22_PCP_JOSE,
  author    = {Meinard M{\"u}ller and Sebastian Rosenzweig},
  title     = {{PCP} Notebooks: {A} Preparation Course for {P}ython with a Focus on Signal Processing},
  journal   = {Journal of Open Source Education ({JOSE})},
  volume    = {5},
  number    = {47},
  year      = {2022},
  pages     = {148:1--5},
  doi       = {10.21105/jose.00148},
  url-demo = {https://github.com/groupmm/PCP}
}
```

## Installing Local Environment for Executing PCP Notebooks
This is the preferred and tested variant for using the PCP notebooks. Install [Miniconda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html), download the [ZIP archive of the latest release](https://github.com/groupmm/PCP/releases/latest) and extract it into a directory named `PCP` (or clone this repository), and run the following commands in a terminal:

```
cd PCP
conda env create -f environment.yml
conda activate PCP
jupyter notebook
```

## Using Web-Based Services for Executing PCP Notebooks

### Google Colab
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/groupmm/PCP/blob/master/PCP.ipynb)

The PCP notebooks may be executed using [Google Colab](https://colab.research.google.com/). However, this needs some preparation. First, you need to be logged in with a Google account. The starting notebook can be accessed via:

https://colab.research.google.com/github/groupmm/PCP/blob/master/PCP.ipynb

For the other notebooks, clone the PCP repository to get access to data and the functions in `libpcp`. To this end, for each Colab session, include and execute a code cell at the beginning of the notebook containing the following lines:

```
%%bash
git clone https://github.com/groupmm/PCP.git PCP_temp
mv PCP_temp/* .
rm -rd PCP_temp
```

### Binder
[![Open In Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/groupmm/PCP/master)

One can also use [Binder](https://mybinder.org/) to execute the PCP notebooks. This clones the repository and automatically creates a conda environment. This may take several (maybe even up to ten) minutes when starting Binder.

https://mybinder.org/v2/gh/groupmm/PCP/master

## Contributing
We are happy for suggestions and contributions. However, to facilitate the synchronization, we would be grateful for either directly contacting us via email (meinard.mueller@audiolabs-erlangen.de) or for creating [an issue](https://github.com/groupmm/PCP/issues) in our GitHub repository. Please do not submit a pull request without prior consultation with us.

## Acknowledgment

The PCP notebooks were first developed together with Sebastian Rosenzweig, whose ideas and contributions played a central role in shaping the course. We want to thank the various people who have contributed to the design, implementation, and code examples of the notebooks. We mention the main contributors in alphabetical order: Vlora Arifi-Müller, Michael Krause, Heinrich Löllmann, Peter Meier, Meinard Müller, Sebastian Rosenzweig, Sebastian Strahl, Frank Zalkow. The [International Audio Laboratories Erlangen](https://www.audiolabs-erlangen.de/) are a joint institution of the [Friedrich-Alexander-Universität Erlangen-Nürnberg (FAU)](https://www.fau.eu/) and [Fraunhofer Institute for Integrated Circuits IIS](https://www.iis.fraunhofer.de/en.html). This work was supported in part by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) through the project "Learning with Music Signals: Technology Meets Education" (Grant No. 500643750, MU 2686/15-1).
