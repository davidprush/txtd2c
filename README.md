<div align="left">

[![Build status](https://github.com/davidprush/keycollator/workflows/build/badge.svg?branch=master&event=push)](https://github.com/davidprush/keycollator/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/keycollator.svg)](https://pypi.org/project/keycollator/)
[![License](https://img.shields.io/github/license/davidprush/keycollator)](https://github.com/davidprush/keycollator/blob/master/LICENSE)

```bash
┬┌─┌─┐┬ ┬┌─┐┌─┐┬  ┬  ┌─┐┌┬┐┌─┐┬─┐
├┴┐├┤ └┬┘│  │ ││  │  ├─┤ │ │ │├┬┘
┴ ┴└─┘ ┴ └─┘└─┘┴─┘┴─┘┴ ┴ ┴ └─┘┴└─
```
<div align="left">

`Compares text in a file to reference/glossary/key-items/dictionary file.`

🧱 Built by 'David Rush <https://github.com/davidprush>'

The latest version of this document can be found at
<https://github.com/davidprush/keycollator/blob/main/README.rst>;
if you are viewing it there (via HTTPS), you can download
the Markdown/reStructuredText source at
<https://github.com/davidprush/keycollator>. You can contact
the author via e-mail at <davidprush@gmail.com>.

## 🗂️ Structure
```bash
.
│
├── assets
│   └── images
│       └── coverage.svg
│
├── docs
│   ├── cli.md
│   └── index.md
│
├── src
│   ├── __init__.py
│   ├── cli.py
│   ├── keycollator.py
│   ├── test_keycollator.py
│   ├── extractonator.py
│   ├── requirements.txt
│   └──data
│       ├── (placeholder)
│       └── (placeholder)
│
├── tests
│   └── test_keycollator
│       ├── __init__.py
│       └── test_keycollator.py
│
├── COD_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── make-venv.sh
├── Makefile
├── pyproject.toml
├── README.README
├── README.rst
├── setup.cfg
└── setup.py
```

## 🚀 Features

- Extract text from file to dictionary
- Extract keys from file to dictionary
- Find matches of keys in text file
- Apply fuzzy matching

## 🧰 Installation

- Future plans to install as python package

```bash
pip install keycollator
```

## 📄 Documentation

Official documentation can be found here:
https://github.com/davidprush

## 💪 Supported File Formats

- TXT/CSV files (Mac/Linux/Win)
- Plans to add PDF and JSON

## 📐 Usage

- Import it into Python Projects

    from keycollator import extractionator

## 🖥️ CLI

keycollator uses the `CLI` to change default parameters and functions

```bash
usage: keycollator.py [-h] [-c CSV_FILE] [-d DICTIONARY_FILE] [-f COUNT]
                  [-i IN_FILE] [-l] [-o OUT_FILE] [-v] [--version]

App takes two files, a dictionary file and a and a text file, and counts
how many times each line in the dictionary file appears in the text file.
The app can output the results to the console and/or csv/text file.
Matching will use fuzzy matching to get desired results.

optional arguments:
-h, --help            show this help message and exit
-c CSV_FILE, --csv-file CSV_FILE
                    Change the csv output file name (defautl is results.csv)
-d DICTIONARY_FILE, --dictionary-file DICTIONARY_FILE
                    Change the dictionary file name (default is dictionary.txt)
-f COUNT, --fuzzy COUNT
                    Select a value for fuzzyness 1-99, 1 for decresed accuracy, 99 for increased
                    accuracy, default is set to 95
-i IN_FILE, --in-file IN_FILE
                    Change the input file name (default is text.txt)
-l, --logging         Set flag to True for logging.
-o OUT_FILE, --out-file OUT_FILE
                    Change the output file name (default is results.txt)
-v, --verbose         Verbosity (-v, -vv, etc)
--version             show version number and exit
```

#### 🖥️ Applying fuzzy matching

    For fuzzy matching use

```bash
keycollator -f=[1-99]
```

#### 🖥️ Setting the dictionary file (simple text file with items separated by line)

```bash
keycollator -d=/path/to/dictionary/directory/
```

#### 🖥️ Create a log file

```bash
keycollator -l=/path/to/log_file/directory/
```

#### 🖥️ Specify the CSV results file

```bash
keycollator -c=/path/to/results/file.csv
```

#### 🖥️ Turn on verbose output

```bash
keycollator -v
```

#### 🖥️ Turn on logging:

```bash
keycollator -l
```

## 🎯 Todo:

    ❌ Currently refactoring all code
    ✅ Separating project into multiple files
    ✅ Add progress bars when extracting and comparing
    📌Create a logger class (for some reason logging is broken)
    ❌ Fix matching method in KeyKrawler
    ❌ Update `README.md(.rst)` with correct CLI
    ❌ Add method to KeyKrawler to select and create missing files
    ❌ Update `CODE_OF_CONDUCT.md`
    ❌ Update `CONTRIBUTING.md`
    ❌ Format KeyCrawler results as a table

## 👔 Project Resource Acknowledgements

    - https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/#creating-a-python-package

    - https://gist.github.com/javiertejero/4585196

## 💼 Deployment Features


## 📈 Releases


## 🛡 License

[![License](https://img.shields.io/github/license/davidprush/keycollator)](https://github.com/davidprush/keycollator/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/davidprush/keycollator/blob/master/LICENSE) for more details.

```bibtex
@misc{keycollator,
  author = {keycollator},
  title = {Compares text in a file to reference/glossary/key-items/dictionary file.},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/davidprush/keycollator}}
}
```
