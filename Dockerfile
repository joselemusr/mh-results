FROM python:3.9.5-slim-buster

WORKDIR /usr/src/results

COPY requirements.txt ./

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install -r requirements.txt

COPY . .

CMD [ "/opt/venv/bin/python3", "./main.py" ]