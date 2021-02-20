# RPi.GPIO template
## Summary
RPi.GPIO template project for the Raspberry Pi.

VS Code is highly recommended.

## Getting started
### Run the project
This project requires Python 3.

First of all you need to create a virtual environment
`python -m venv env`

Activate you virtual environment
`source env/bin/activate`

Install dependencies
`python -m pip install -r requirements/dev.txt`

### Install the module
To locally install the module you can execute the following command from the root of the project
`python -m pip install -e .`

Once installed you can execute it by typing the name of the module in the command line, You can find the name of the command line in the `setup.py` file `entry_point` section.
