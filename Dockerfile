#Dockerfile
FROM python:3.8

ADD testingBinance.py

RUN pip install requests pandas numpy

CMD ["python3", "./testingBinance.py"]
