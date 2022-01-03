FROM python:3.9-alpine

WORKDIR /home

COPY . ./
# COPY requirements.txt ./
# COPY *.py ./
# COPY *.sql ./
# COPY database ./database
# COPY handlers ./handlers
# COPY keyboards ./keyboards

# RUN pip install -U pip install --no-cache-dir -r requirements.txt && apt-get update && apt-get install sqlite3
RUN pip install -U pip install --no-cache-dir -r requirements.txt && apk update && apk add sqlite

ENTRYPOINT ["python", "server.py"]