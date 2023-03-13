FROM python:latest
LABEL Maintainer="Tommy Ng"

#WORKDIR ./src
COPY src/scispacy.py ./
COPY src/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
USER 10014

CMD [ "python", "./scispacy.py" ]
