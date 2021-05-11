#!/bin/bash

rm -r build; rm -r *.egg-info; rm -r dist
pip install --upgrade build twine
python -m build --sdist --wheel .
python -m twine upload --non-interactive -u "__token__" -p "$PYPI_TOKEN" --repository testpypi dist/*
