#!/bin/bash

exec uvicorn --host 0.0.0.0 --port 5000 --log-level=debug --reload main:app
