#!/bin/bash

ENV_DIR="venv"
REQUIREMENTS_FILE="requirements.txt"
PYTHON_SCRIPT="client.py"

if [ -d "$ENV_DIR" ]; then
    echo "Removing existing virtual environment directory..."
    rm -rf "$ENV_DIR"
fi

echo "Creating a new virtual environment..."
python3 -m venv "$ENV_DIR"

echo "Activating the virtual environment..."
source "$ENV_DIR/bin/activate"

echo "Upgrading pip..."
pip install --upgrade pip

if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing packages from $REQUIREMENTS_FILE..."
    pip install -r "$REQUIREMENTS_FILE"
else
    echo "Error: $REQUIREMENTS_FILE not found!"
    exit 1
fi

echo ""
echo ""
if [ -f "$PYTHON_SCRIPT" ]; then
    echo "Running the Python script $PYTHON_SCRIPT..."
    python "$PYTHON_SCRIPT"
else
    echo "Error: $PYTHON_SCRIPT not found!"
    exit 1
fi

deactivate

