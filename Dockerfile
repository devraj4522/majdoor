FROM python:3
WORKDIR D:/majdoor
ADD requirements.txt D:/majdoor
RUN pip install -r requirements.txt
ADD  . D:/majdoor