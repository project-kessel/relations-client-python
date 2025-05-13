#!/bin/bash

# Check if argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <new_version>"
  CURRENT_VERSION=$(grep -Eo "version = [0-9]+\.[0-9]+\.[0-9]+" setup.cfg | awk '{print $3}')
  echo "Current version is: $CURRENT_VERSION"
  exit
fi

NEW_VERSION=$1
VENV_DIR="venv"
DIST_DIR="dist"

# Cross-platform sed version bump
echo "Updating version in setup.cfg to $NEW_VERSION"
if [[ "$OSTYPE" == "darwin"* ]]; then
  sed -i '' "s/^version = .*/version = $NEW_VERSION/" setup.cfg
else
  sed -i "s/^version = .*/version = $NEW_VERSION/" setup.cfg
fi

# Check if virtual environment directory exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtual environment not found. Creating one..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build twine

# Remove old distribution files
echo "Removing old distribution files..."
rm -rf $DIST_DIR

# Build the distribution
echo "Building the distribution..."
python3 -m build

# Upload the distribution to PyPI
echo "Uploading the distribution to PyPI..."
twine upload "$DIST_DIR"/*

# Deactivate the virtual environment
deactivate

echo "Package successfully uploaded to PyPI!"
