# QA Automation & CI/CD

Practical project focused on software quality assurance, automated testing and continuous integration using Python and modern QA tools.

## Project overview

This project implements a REST API using Flask and validates its behavior through automated tests with pytest.

The objective is to build a practical testing workflow covering API validation, test automation, performance testing and continuous integration.

## Technologies

- **Python 3.12**
- **Flask** – REST API development
- **pytest** – Automated testing
- **Git / GitHub** – Version control and source code management
- **Jenkins** – Continuous integration
- **k6** – Performance and load testing

## API endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks API availability |
| POST | `/api/sum` | Adds two numeric values received as JSON |

### Example request

`POST /api/sum`

```json
{
  "a": 10,
  "b": 20
}
```

Expected response:

```json
{
  "result": 30
}
```

## Automated tests

The test suite currently validates:

- API health check.
- Successful calculation with numeric values.
- Missing request parameters.
- Invalid parameter types.
- Boolean values rejected as numeric input.

Run the tests:

```bash
python -m pytest -v
```

## Project structure

```text
qa-automation-ci/
│
├── app.py
├── test_app.py
├── requirements.txt
├── .gitignore
├── performance/
│   └── load_test.js
└── Jenkinsfile
```

## Project status

The REST API and initial automated test suite are implemented.

Further development focuses on performance testing with k6 and continuous integration with Jenkins.