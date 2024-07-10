#!/bin/bash

# Install dependencies if needed
pip install -r requirements.txt

# Run coverage
coverage run -m unittest discover -s tests -v

# Generate coverage report
coverage report -m --omit="*/tests/*"
