# Python System Info API

> A clean, minimalist Flask application demonstrating system monitoring with Docker and CI/CD.

![Dashboard](screenshots/dashboard.png)

## Features

- **Real-time Dashboard**: Beautiful gradient UI with live metrics
- **REST API**: JSON endpoints for system health and metrics
- **Dockerized**: Production-ready containerization
- **CI/CD**: Automated testing with GitHub Actions
- **Monitoring**: Optional Prometheus + Grafana stack

## Quick Start

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python -m flask --app app run

# Open browser
http://localhost:5000
```

### Docker
```bash
# Build and run
docker build -t python-system-info .
docker run -p 5000:5000 python-system-info

# With monitoring stack
docker compose -f docker-compose.monitoring.yml up
```

## API Endpoints

- `GET /` - Dashboard UI
- `GET /health` - Health check (JSON)
- `GET /info` - Detailed system metrics (JSON)

## Project Structure
```
python-system-info/
├── .github/workflows/    # CI/CD pipelines
├── app/
│   ├── __init__.py       # Flask app factory
│   ├── routes.py         # API endpoints
│   └── templates/
│       └── dashboard.html
├── Dockerfile
├── requirements.txt
└── README.md
```

## Refactoring Notes

This is a simplified version of a larger AWS-deployed application. Key improvements:
- Removed AWS EC2 deployment complexity
- Migrated from GitLab CI to GitHub Actions
- Added real-time monitoring dashboard
- Containerized for local-first development

See [REFACTORING.md](https://github.com/imartinez-88/python-system-info/blob/main/REFACTORING.md) for details.
