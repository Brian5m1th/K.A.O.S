FROM python:3.13-slim AS builder

WORKDIR /app

COPY pyproject.toml ./

RUN pip install uv && \
    uv venv /app/.venv && \
    VIRTUAL_ENV=/app/.venv uv pip install torch --index-url https://download.pytorch.org/whl/cpu && \
    VIRTUAL_ENV=/app/.venv uv sync --no-dev

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY app/ /app/app/
RUN touch /app/.env

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]