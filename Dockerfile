FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY \
    .python-version \
    uv.lock \
    pyproject.toml \
    /app/

# Install uv
RUN apt-get update && apt-get install -y curl build-essential
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="$PATH:/root/.local/bin"

# Install project dependencies
RUN uv sync --no-dev
COPY warmup.py /app
RUN uv run python warmup.py
RUN rm warmup.py

COPY main.py  /app
EXPOSE 8000

CMD ["uv", "run", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--reload"]