# Gaussian to XYZ Converter

This repository contains a Python script (`gaussian2xyz.py`) that is designed to read Gaussian output files (`.log` files) and extract the geometrically optimized structure, writing it to a standard XYZ format file.

## Features

- **Read Gaussian Output**: Automatically finds and reads the Gaussian output file in the current directory.
- **Extract Optimized Geometry**: Parses the 'Standard orientation' section from the Gaussian output.
- **Write to XYZ Format**: Outputs the atomic coordinates in the widely-supported XYZ format.

## Usage

To use this script, simply place it in the same directory as your Gaussian `.log` files and run it using Python. The script will automatically detect the `.log` file, extract the optimized geometry, and write it to an `output.xyz` file.

### Step-by-Step Instructions

1. Ensure that you have Python3 installed on your system. You can download Python from [here](https://www.python.org/downloads/).
2. Place the `gaussian2xyz.py` script in the directory containing your Gaussian `.log` files.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script and log files.
5. Run the script:
   ```bash
   python gaussian2xyz.py
6. Check the directory for the 'output.xyz' file, which will contain the converted coordinates.

## Requirements

- Python 3.x

## License

This project is open source and available under the MIT License.
