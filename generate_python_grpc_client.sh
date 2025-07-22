#!/bin/bash

set -e

echo "Creating and activating the virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "Installing the specific relations API python client from Buf"
python3 -m pip install --upgrade pip
python3 -m pip install project-kessel-relations-api-grpc-python==1.73.1.1.20250721151001+f2961badb6b4 --extra-index-url https://buf.build/gen/python

echo "Copying files to necessary directory for buf validation files"
mkdir -p src/buf/validate
touch src/buf/__init__.py
touch src/buf/validate/__init__.py
cp -r venv/lib/python*/site-packages/buf/validate/* src/buf/validate

echo "Copying files to necessary directory for relations API"
mkdir -p src/kessel/relations/v1beta1
cp -r venv/lib/python*/site-packages/kessel/relations/v1beta1/* src/kessel/relations/v1beta1/

echo "Deactivating the virtual environment"
deactivate

echo "Removing the virtual environment"
rm -rf venv

echo "Python client successfully updated to new version"
