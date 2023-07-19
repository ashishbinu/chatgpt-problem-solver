# Build image
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app
COPY . .

# Install project dependencies using pip
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN $HOME/.local/bin/poetry config virtualenvs.create false 
RUN $HOME/.local/bin/poetry export -f requirements.txt >> requirements.txt

# Prod image
FROM python:3.11-slim-bullseye AS runtime

RUN mkdir /app
WORKDIR /app

COPY --from=builder /app/. .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
