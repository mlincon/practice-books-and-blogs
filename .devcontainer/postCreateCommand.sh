#!/bin/bash

# install pre-commit
pre-commit install

# create and install libraries for Llama Index
conda create -y --name llamaIndex python=3.11
conda init
conda activate llamaIndex && \
    pip install -r courses/Marco-LlamaIndex/requirements.txt
