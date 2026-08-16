-- Create database for Tesla telemetry ETL project
CREATE DATABASE IF NOT EXISTS TESLA_TELEMETRY_DB;

-- Use the database
USE DATABASE TESLA_TELEMETRY_DB;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS RAW;

CREATE SCHEMA IF NOT EXISTS CURATED;

-- Use curated schema for transformed analytical data
USE SCHEMA CURATED;
