FROM python:3.9-slim-bullseye AS builder

# setup virtualenv, copy and install requirements
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.9-slim-bullseye

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"