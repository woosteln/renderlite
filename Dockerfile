FROM python:3.6-alpine

RUN mkdir /src
WORKDIR /src
ADD . /src

RUN pip install -r requirements.txt

CMD ["python", "__main__.py"]