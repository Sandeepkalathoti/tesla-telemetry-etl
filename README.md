# Tesla Telemetry ETL Pipeline

An end-to-end data engineering project for processing Tesla vehicle telemetry data using Python, Apache Airflow, Snowflake, Docker, Pytest, and GitHub Actions.

## Project Overview

This project demonstrates a production-style ETL pipeline that extracts Tesla vehicle telemetry data from JSONL files, validates and transforms the data using Python, and prepares it for loading into Snowflake.

Apache Airflow is used to orchestrate the ETL workflow, while Pytest is used for automated testing and GitHub Actions provides CI automation.

## Architecture

```text
Tesla Telemetry JSONL
        |
        v
    Extract
        |
        v
   Transform
        |
        v
 Data Quality
        |
        v
      Load
        |
        v
    Snowflake
        |
        v
 Curated Models

Apache Airflow
      |
      +---- Extract
      +---- Transform
      +---- Quality
      +---- Load

GitHub Actions
      |
      +---- Install Dependencies
      +---- Run Tests

## TECHNOLOGY STACK

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | ETL development        |
| Apache Airflow | Workflow orchestration |
| Snowflake      | Cloud data warehouse   |
| SQL            | Data modeling          |
| Pytest         | Automated testing      |
| Docker         | Containerization       |
| GitHub Actions | CI/CD                  |
| JSONL          | Source data format     |

##PROJECT STRUCTURE

tesla-telemetry-etl/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── dags/
│   └── tesla_telemetry_etl_dag.py
│
├── data/
│   └── sample/
│       └── tesla_telemetry_sample.jsonl
│
├── docs/
│   ├── architecture.md
│   └── data_dictionary.md
│
├── snowflake/
│   ├── 001_create_database_schema.sql
│   ├── 002_create_tables.sql
│   └── 003_curated_models.sql
│
├── src/
│   └── telemetry_etl/
│       ├── config.py
│       ├── extract.py
│       ├── load.py
│       ├── quality.py
│       ├── schemas.py
│       └── transform.py
│
├── tests/
│   ├── test_quality.py
│   └── test_transform.py
│
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
├── .env.example
└── .gitignore

##ETL Workflow
1. Extract
Telemetry data is read from a JSONL file.
The extraction module:
Reads the source file.
Parses each JSON record.
Validates JSON structure.
Returns telemetry records as Python dictionaries.

2. Transform
The transformation layer:
Standardizes vehicle IDs.
Converts timestamps into Python datetime objects.
Converts numeric fields into appropriate numeric types.
Produces a standardized telemetry structure.

3. Data Quality
The quality layer validates:
Required fields
Vehicle ID
Speed
Battery percentage
Latitude
Longitude
Timestamp
Invalid records are separated from valid records.

4. Load
Validated records are prepared for loading into Snowflake.
The Snowflake data model contains:
Raw telemetry table
Curated telemetry table
Vehicle-level telemetry summary view

5. Orchestration
Apache Airflow manages the ETL workflow:
Extract → Transform → Quality → Load
The DAG is configured to run daily.

##Snowflake Data Model
Database
TESLA_TELEMETRY_DB

Schemas
RAW
CURATED

Raw Table
TESLA_TELEMETRY_RAW

Curated Table
TESLA_TELEMETRY

Curated View
TESLA_TELEMETRY_SUMMARY

The summary view provides vehicle-level metrics such as:
Total telemetry events
Average speed
Maximum speed
Average battery level
Minimum battery level
First event timestamp
Last event timestamp

##Testing
The project uses Pytest for automated testing.

##Tests cover:
Valid telemetry records
Invalid speed values
Invalid battery levels
Invalid latitude values
Invalid longitude values
Missing vehicle IDs
Multiple telemetry records

##Transformation logic
Run tests locally using:
pytest

##Running with Docker
Start the Airflow environment using:
docker compose up -d

Airflow UI:
http://localhost:8080
The project uses Docker volumes to make DAGs, source code, sample data, and tests available inside the Airflow container.

##Environment Configuration

Create a local .env file based on .env.example.
Do not commit real credentials or secrets to GitHub.

Example:
SNOWFLAKE_ACCOUNT=your_account_identifier
SNOWFLAKE_USER=your_username
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_WAREHOUSE=your_warehouse

##CI/CD

GitHub Actions automatically runs the project tests when changes are pushed to the main branch or when a pull request is created.

Workflow:

Git Push / Pull Request
          |
          v
    Checkout Code
          |
          v
    Setup Python
          |
          v
 Install Dependencies
          |
          v
       Run Pytest

##Future Improvements
Add real Tesla telemetry ingestion.
Integrate AWS S3 as the source layer.
Add Snowflake bulk loading using stages and COPY INTO.
Add incremental loading.
Add data partitioning.
Add monitoring and alerting.
Add Airflow retries and failure notifications.
Add Terraform infrastructure provisioning.
Add dbt models for the curated layer.
Add dashboard integration using Power BI or Tableau.

