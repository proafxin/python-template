# Python Template

[![Build, test with Tox and deploy](https://github.com/proafxin/python-template/actions/workflows/test_release.yaml/badge.svg)](https://github.com/proafxin/python-template/actions/workflows/test_release.yaml)
[![codecov](https://codecov.io/gh/proafxin/python-template/graph/badge.svg?token=w6t9xzSY45)](https://codecov.io/gh/proafxin/python-template)

A template for building python packages with CI/CD for code quality check and publishing to PyPi.

## Development

You need [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) and [Tox](https://tox.wiki/en/latest/installation.html#via-pip) preinstalled.

## Publishing to Pypi

First, you should always update your version using [semantic versioning](https://packaging.python.org/en/latest/discussions/versioning/#semantic-versioning) as PyPi does not allow overwriting existing packages. Run one of the following based on your changes

- `poetry version major`
- `poetry version minor`
- `poetry version patch`

This template uses Github Actions for publishing to PyPi. So, you also need `PYPI_TOKEN` available as a respository secret.
