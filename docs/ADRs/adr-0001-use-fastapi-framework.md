# ADR-0001: Use FastAPI as Backend Framework

## Status
Accepted

## Context

PCBuilderBR is a web application that helps users in Brazil select compatible PC components and find the best prices from local retailers. The backend needs to:

- Expose REST APIs for component management and compatibility validation
- Handle asynchronous tasks for scheduled price updates from multiple retailers (Kabum, Pichau, Amazon)
- Support Pydantic models for request/response validation
- Provide interactive API documentation for frontend integration
- Run background jobs for price fetching on a daily schedule

## Decision

We will use **FastAPI** as the backend framework.

## Alternatives Considered

### Flask
- Well-known Python framework
- Requires manual request validation
- No built-in async support (depends on extensions)
- Less modern tooling ecosystem

### Django
- Full-featured framework with batteries included
- Heavy weight for an API-only project
- Steeper learning curve for team
- Overkill for our requirements

### NestJS (TypeScript)
- Excellent dependency injection
- Strong TypeScript integration
- Requires separate runtime (Node.js)
- Team familiarity with Python

## Consequences

### Positive
- Native async/await support for handling concurrent retailer API calls
- Automatic OpenAPI/Swagger documentation at `/docs`
- Built-in Pydantic validation for request/response models
- Automatic JSON schema generation for frontend type safety
- Lightweight with minimal boilerplate
- Easy background job scheduling with APScheduler integration

### Negative
- Smaller ecosystem compared to Django
- Less mature admin panel compared to Django

### Neutral
- Python dependency (shares language with data analysis scripts)
- Requires async awareness when writing services

## Related ADRs
N/A - First ADR

## Notes
- FastAPI chosen for rapid development and excellent DX
- Pydantic integration provides type safety end-to-end
