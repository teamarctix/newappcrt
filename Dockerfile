FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv && pipenv install
RUN curl https://cli-assets.heroku.com/install.sh | sh
COPY *.py .
CMD [ "python", "main.py" ]
