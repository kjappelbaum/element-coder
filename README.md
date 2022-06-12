<!--
<p align="center">
  <img src="https://github.com/kjappelbaum/element-coder/raw/main/docs/source/logo.png" height="150">
</p>
-->

<h1 align="center">
  element_coder 
</h1>

<p align="center">
    <a href="https://github.com/kjappelbaum/element-coder/actions?query=workflow%3ATests">
        <img alt="Tests" src="https://github.com/kjappelbaum/element-coder/workflows/Tests/badge.svg" />
    </a>
    <a href="https://github.com/cthoyt/cookiecutter-python-package">
        <img alt="Cookiecutter template from @cthoyt" src="https://img.shields.io/badge/Cookiecutter-python--package-yellow" /> 
    </a>
    <a href="https://pypi.org/project/element_coder">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/element_coder" />
    </a>
    <a href="https://pypi.org/project/element_coder">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/element_coder" />
    </a>
    <a href="https://github.com/kjappelbaum/element-coder/blob/main/LICENSE">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/element_coder" />
    </a>
    <a href='https://element_coder.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/element_coder/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
</p>

Encode chemical elements numerically and decode numerical representations of elements.

## 💪 Getting Started

```python
from element_coder import encode, decode 

decode(encode('Si', 'mod_pettifor'), 'mod_pettifor')
>'Si'
```

### Command Line Interface

The `element_coder.encode` and `element_coder.decode` command line tools are automatically installed. They can
be used from the shell with the `--help` flag to show help:

```shell
$ element_coder.encode H
102
```

```shell
$ element_coder.decode 102
H
```

also works for vector-valued encodings

```shell
$ element_coder.decode 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 --property cgcnn
H
```

## 🚀 Installation


The most recent release can be installed from
[PyPI](https://pypi.org/project/element_coder/) with:

```bash
$ pip install element_coder
```

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/kjappelbaum/element-coder.git
```

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/kjappelbaum/element-coder.git
$ cd element-coder
$ pip install -e .
```

## Background
For some applications (of ML in chemistry) elements must be numerically encoded. There are many libraries that do that. For most applications, even [pymatgen](www.pymatgen.org) can get the job done: 

```python
from pymatgen.core import Element
def encode_element(element: Element, property: str): 
    return getattr(element, property)
```

However, this code has some issues, wherefore there are many other libraries that attempt to solve this issue including [mendeleev](https://github.com/lmmentel/mendeleev), [elementy](https://github.com/Robert-Forrest/elementy), [EIMD](https://github.com/lrcfmd/ElMD). However, 

* none of these libraries supported all the properties I was interested in 
* none of these libraries supported decoding of descriptors into Elements.

## 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.rst](https://github.com/kjappelbaum/element-coder/blob/master/CONTRIBUTING.rst) for more information on getting involved.

## 👋 Attribution

### ⚖️ License

The code in this package is licensed under the MIT License.

<!--
### 📖 Citation

Citation goes here!
-->

<!--
### 🎁 Support

This project has been supported by the following organizations (in alphabetical order):

- [Harvard Program in Therapeutic Science - Laboratory of Systems Pharmacology](https://hits.harvard.edu/the-program/laboratory-of-systems-pharmacology/)

-->

<!--
### 💰 Funding

This project has been supported by the following grants:

| Funding Body | Program                                                                                                                       | Grant         |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------------- |
| DARPA        | [Automating Scientific Knowledge Extraction (ASKE)](https://www.darpa.mil/program/automating-scientific-knowledge-extraction) | HR00111990009 |
-->

### 🍪 Cookiecutter

This package was created with [@audreyfeldroy](https://github.com/audreyfeldroy)'s
[cookiecutter](https://github.com/cookiecutter/cookiecutter) package using [@cthoyt](https://github.com/cthoyt)'s
[cookiecutter-snekpack](https://github.com/cthoyt/cookiecutter-snekpack) template.

## 🛠️ For Developers

<details>
  <summary>See developer instrutions</summary>

  
The final section of the README is for if you want to get involved by making a code contribution.

### ❓ Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/kjappelbaum/element-coder/actions?query=workflow%3ATests).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses BumpVersion to switch the version number in the `setup.cfg` and
   `src/element_coder/version.py` to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel
3. Uploads to PyPI using `twine`. Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion minor` after.
</details>
