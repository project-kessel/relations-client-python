#!/bin/bash

echo "Creating and activating the virtual environment"
python3 -m venv venv
source venv/bin/activate

echo "Installing the relations api python client"
python3 -m pip install project-kessel-relations-api-grpc-python --extra-index-url https://buf.build/gen/python

echo "Copying files to necessary directory for buf validation files"
mkdir -p src/buf/validate
cp -r venv/lib/python*/site-packages/buf/validate/* src/buf/validate

echo "Copying files to necessary directory"
mkdir -p src/kessel/relations/v1beta1
cp -r venv/lib/python*/site-packages/kessel/relations/v1beta1/* src/kessel/relations/v1beta1/

echo "Deactivating the virtual environment"
deactivate
echo "Removing the virtual environment"
rm -rf "venv"

echo "python client successfully updated"
