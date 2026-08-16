# Tesla Telemetry ETL Architecture

## Overview

This project implements an end-to-end ETL pipeline for processing Tesla vehicle telemetry data.

The pipeline follows these stages:

1. Extract telemetry data from JSONL files.
2. Validate and transform the raw data using Python.
3. Apply data quality checks.
4. Load processed data into Snowflake.
5. Orchestrate the pipeline using Apache Airflow.
6. Run automated tests using Pytest.
7. Use GitHub Actions for continuous integration.

## Architecture

```text
Tesla Telemetry JSONL
        |
        v
   Extract Layer
        |
        v
 Transform Layer
        |
        v
 Quality Checks
        |
        v
   Load Layer
        |
        v
     Snowflake
        |
        v
 Curated Data Models

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
