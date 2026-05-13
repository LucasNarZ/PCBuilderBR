# PCBuilderBR

PCBuilderBR is a web application for planning PC builds in Brazil. It helps users choose components, compare prices, and validate whether the selected parts are compatible before buying.

## Features

- Component selection for CPU, motherboard, RAM, GPU, storage, PSU, case, coolers, monitors, and peripherals.
- Compatibility checks for sockets, RAM type, GPU clearance, PSU capacity, connectors, and case constraints.
- Build price summary based on the selected parts.
- Product and price tracking from major Brazilian retailers.
- Recommended builds and shareable configurations are planned for future releases.

## Tech Stack

- Frontend: React, Vite, TypeScript, Tailwind CSS, Axios.
- Backend: FastAPI, Pydantic, SQLAlchemy, Alembic.
- Database: PostgreSQL.
- Infrastructure: Docker Compose, Nginx, Grafana, Loki, Promtail, pgAdmin.

## Running Locally

### Prerequisites

- Docker and Docker Compose.
- Node.js and npm, if you want to use the root helper scripts.

### Setup

1. Copy the environment example:

```bash
cp .env.example .env
```

2. Adjust the values in `.env` if needed.

3. Start the development environment:

```bash
npm run dev:up
```

4. Follow the logs:

```bash
npm run dev:logs
```

5. Stop the environment:

```bash
npm run dev:down
```

The development compose file exposes PostgreSQL on port `5432`, pgAdmin on port `5050`, and routes the application through Nginx on ports `80` and `443`.

## Useful Scripts

- `npm run dev:up`: starts the development stack.
- `npm run dev:down`: stops the development stack.
- `npm run dev:logs`: follows logs from the development stack.
- `npm run dev:ps`: lists running development services.
- `npm run prod:up`: starts the production stack.

## Project Structure

```text
.
├── backend/      # FastAPI application, database models, migrations, and workers
├── frontend/     # React and Vite application
├── infra/        # Observability configuration
├── docs/         # Architecture documentation
├── nginx.dev.conf
├── docker-compose.dev.yml
└── docker-compose.prod.yml
```

## Roadmap

- Weekly price updates using retailer APIs or catalog integrations.
- Price history per product and store.
- Performance estimates for popular games.
- Build sharing by public link.
- Export builds as CSV or JSON.
- PSU consumption calculation with safety margin recommendations.
