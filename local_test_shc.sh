# navigate to root directory and activate virtual environment:
# source venv/bin/activate
# run the tests:
# bash local_test_shc.sh


# Install dependencies if needed
pip install -r requirements.txt

# Run coverage
coverage run -m unittest discover -s tests -v

# Generate coverage report
coverage report -m --omit="*/tests/*"
