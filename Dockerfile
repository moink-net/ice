FROM docker.io/library/python:alpine

WORKDIR /opt/ice
COPY . ./
RUN python -m pip install -r requirements.txt
ENTRYPOINT ["python","ice.py"]

EXPOSE 8080
