FROM ghcr.io/astral-sh/uv:0.12.23-python3.14-alpine

WORKDIR /api

ENV PATH="/api/.venv/bin:$PATH" \
  API_ENV=prod \
  PYTHONUNBUFFERED=1

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "main:app", "--access-logfile", "-", "--error-logfile", "-", "--log-level", "info"]
