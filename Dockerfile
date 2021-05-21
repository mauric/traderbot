#Dockerfile
FROM continuumio/anaconda3

WORKDIR .
COPY . . 

CMD ["python3", "./testingBinance.py"]
