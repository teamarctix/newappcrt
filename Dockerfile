FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv && pipenv install
COPY *.py .
CMD [ "python", "main.py" ]
