FROM continuumio/miniconda3:4.10.3p0-alpine

RUN pip install mlflow>=1.18.0 \
    && pip install numpy \
    && pip install scipy \
    && pip install pandas \
    && pip install scikit-learn \
    && pip install cloudpickle \
    && pip install pandas_datareader==0.10.0 \
    && pip install yfinance