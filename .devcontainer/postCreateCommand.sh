#!/bin/bash

# install pre-commit
pre-commit install

# prepare shell for condas
conda init

# create and install libraries for Llama Index
conda create -y --name llamaIndex python=3.11
conda activate llamaIndex && \
    pip install -r courses/Marco-LlamaIndex/requirements.txt
