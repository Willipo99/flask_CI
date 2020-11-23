FROM python:slim

RUN pip3 install flask
RUN pip3 install redis

ADD flaskapp.py .
ADD test_basics.py .

CMD ["python", "flaskapp.py"]