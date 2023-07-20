# Build image
FROM python:3.11-slim-bullseye AS builder

WORKDIR /app

# Install project dependencies using pip
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN $HOME/.local/bin/poetry config virtualenvs.create false 

COPY pyproject.toml .
COPY poetry.lock .

RUN $HOME/.local/bin/poetry export -f requirements.txt >> requirements.txt

COPY . .

# Prod image
FROM python:3.11-slim-bullseye AS runtime

RUN mkdir /app
WORKDIR /app

COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --from=builder /app/. .
CMD ["python", "main.py"]
