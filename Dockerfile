FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

USER root
COPY requirements.txt .
RUN eho "Hello Hillel"
RUN python3 -m pip install --upgrade pip
RUN pip install -r /requirements.txt

