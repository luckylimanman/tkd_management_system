FROM python:3.7

WORKDIR /service/tkd_management_system/

ADD . /service/tkd_management_system/

RUN pip install -r requirements.txt

ENV FLASK_APP=tkd_gym

CMD [ "flask", "run", "--host=0.0.0.0"]
