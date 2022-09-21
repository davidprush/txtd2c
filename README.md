<div align="left">

[![Build status](https://github.com/davidprush/keycollator/workflows/build/badge.svg?branch=master&event=push)](https://github.com/davidprush/keycollator/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/keycollator.svg)](https://pypi.org/project/keycollator/)
[![License](https://img.shields.io/github/license/davidprush/keycollator)](https://github.com/davidprush/keycollator/blob/master/LICENSE)

```bash
┬┌─┌─┐┬ ┬┌─┐┌─┐┬  ┬  ┌─┐┌┬┐┌─┐┬─┐
├┴┐├┤ └┬┘│  │ ││  │  ├─┤ │ │ │├┬┘
┴ ┴└─┘ ┴ └─┘└─┘┴─┘┴─┘┴ ┴ ┴ └─┘┴└─
```

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

### 🖥️ Install from **Pypi** using pip3

📦 <https://pypi.org/project/keycollator/0.0.1/>

```bash
pip3 install keycollator
```

## 📄 Documentation

Official documentation can be found here:
https://github.com/davidprush

## 💪 Supported File Formats

- TXT/CSV files (Mac/Linux/Win)
- Plans to add PDF and JSON

## 📐 Usage

### 🖥️ Import _keycollator_ it into Python Projects

```
from keycollator import ZTimer, KeyKrawler
```

## 🖥️ CLI

keycollator uses the `CLI` to change default parameters and functions

```bash
Usage: keycollator.py [OPTIONS] COMMAND [ARGS]...

  keycollator is an app that finds occurances of keys in a text file

Options:
  -v, --set-verbose               Turn on verbose
  -f, --fuzzy-matching INTEGER RANGE
                                  Find valid matches using edit distances or
                                  approximate matches, uses acceptance ratio
                                  of integer values from 0 to 99, where 99 is
                                  near identical  [0<=x<=99]
  -k, --key-file PATH             Path/file name of the key file containing a
                                  dictionary, key items, glossary, or
                                  reference list used to search the text file
  -t, --text-file PATH            Path/file name of the text to be searched
                                  for against items in the key file
  -o, --output-file PATH          Path/file name of the output file that
                                  will contain the results (CSV or TXT)
  -U, --ubound-limit INTEGER RANGE
                                  Ignores items from the results with matches
                                  greater than the upper boundary (upper-
                                  limit); reduce eroneous matches
                                  [1<=x<=99999]
  -L, --lbound-limit INTEGER RANGE
                                  Ignores items from the results with matches
                                  less than the lower boundary (lower-limit);
                                  reduce eroneous matches  [0<=x<=99999]
  -l, --set-logging               Turn on logging
  -Z, --log-file PATH             Path/file name to be used for the log file
  --help                          Show this message and exit.
```

#### 🖥️ Applying _fuzzy matching_

```bash
keycollator -f=[1-99]
```

#### 🖥️ Setting the dictionary file (simple text file with items separated by line)

```bash
keycollator -d=/path/to/dictionary/directory/
```

#### 🖥️ Create a _log file_

```bash
keycollator -l=/path/to/log_file/directory/
```

#### 🖥️ Specify the CSV results file

```bash
keycollator -c=/path/to/results/file.csv
```

#### 🖥️ Turn on _verbose_ output

```bash
keycollator -v
```

#### 🖥️ Turn on _logging_:

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
    ❌ Create ZLog class in extractonator.py
    ❌ Cleanup verbose output
    ❌ Update all comments
    ❌ Migrate click functionality to cli.py


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
