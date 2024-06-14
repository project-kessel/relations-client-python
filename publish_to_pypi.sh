#!/bin/bash

# Check if argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>"
  CURRENT_VERSION=$(grep -Eo "version = [0-9]+\.[0-9]+\.[0-9]+" setup.cfg | awk '{print $3}')
  echo "Current version is: $CURRENT_VERSION"
  exit
fi


# Set variables
VENV_DIR="venv"
DIST_DIR="dist"

NEW_VERSION=$1

# Update the version in setup.cfg using sed
sed -i '' 's/^version = .*/version = '"$NEW_VERSION"'/' setup.cfg

# Check if virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Check if the bump2version command succeeded
if [ $? -ne 0 ]; then
    echo "Failed to bump the version. Aborting."
    exit 1
fi

# Remove old distribution files
echo "Removing old distribution files..."
rm -rf $DIST_DIR

# Build the distribution
echo "Building the distribution..."
python3 -m build

# Upload the distribution to PyPI
echo "Uploading the distribution to PyPI..."
twine upload $DIST_DIR/*

# Deactivate the virtual environment
deactivate

# Check the exit status of the twine upload
if [ $? -ne 0 ]; then
    echo "Failed to upload the package to PyPI. Aborting."
    exit 1
fi

echo "Package successfully uploaded to PyPI!"
