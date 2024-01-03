#!/bin/bash

# install pre-commit
pre-commit install

# pull latest changes
git pull --rebase --all
