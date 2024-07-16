#!/bin/bash

set -e

GITHUB_REPO_URL="https://github.com/project-kessel/relations-api"
PROTO_FOLDER="api/kessel/relations/v1beta1"
TEMP_DIR=$(mktemp -d)
VENV_DIR="$TEMP_DIR/venv"
OUTPUT_DIR=$(pwd)

function cleanup {
  echo "Cleaning up temporary files..."
  rm -rf "$TEMP_DIR"
  echo "Done."
}

trap cleanup EXIT

cd "$TEMP_DIR"

echo "Initializing an empty repository and setting sparse-checkout for $PROTO_FOLDER"
git init
git remote add origin "$GITHUB_REPO_URL"
git config core.sparseCheckout true

echo "$PROTO_FOLDER/*" >> .git/info/sparse-checkout
echo "third_party/*" >> .git/info/sparse-checkout

git pull origin main

if command -v python3 &>/dev/null; then
  PYTHON_CMD=python3
elif command -v python &>/dev/null; then
  PYTHON_CMD=python
else
  echo "Python is not installed. Please install Python and try again."
  exit 1
fi

echo "Using Python command: $PYTHON_CMD"

echo "Creating Python virtual environment..."
$PYTHON_CMD -m venv "$VENV_DIR"

source "$VENV_DIR/bin/activate"

echo "Installing required packages..."
pip install grpcio-tools

echo "Generating Python client from proto files..."

$PYTHON_CMD -m grpc_tools.protoc \
            -I"$TEMP_DIR/third_party/"  \
            -Ikessel/relations/v1beta1="$TEMP_DIR/$PROTO_FOLDER"  \
            --python_out="$OUTPUT_DIR"/src \
            --pyi_out="$OUTPUT_DIR"/src \
            --grpc_python_out="$OUTPUT_DIR"/src \
            "$TEMP_DIR/$PROTO_FOLDER"/*.proto \
            "$TEMP_DIR/third_party/validate/"validate.proto

echo "Python client generated in $TEMP_DIR"

echo "Deactivating and removing the virtual environment..."
deactivate
rm -rf "$VENV_DIR"

find "$TEMP_DIR" -name "*.py"

echo "Script completed successfully."
