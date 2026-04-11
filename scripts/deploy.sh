#!/bin/bash
set -euo pipefail

PROJECT_DIR="${DEPLOY_PATH:-$HOME/PCBuilderBR}"
COMPOSE_FILE="docker-compose.prod.yml"

cd "$PROJECT_DIR"

git fetch origin main
git reset --hard origin/main

docker compose -f "$COMPOSE_FILE" build
docker compose -f "$COMPOSE_FILE" up -d --remove-orphans
docker compose -f "$COMPOSE_FILE" exec -T api uv run alembic upgrade head
