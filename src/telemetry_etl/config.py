import os


DATA_FILE = os.getenv(
    "DATA_FILE",
    "data/sample/tesla_telemetry_sample.jsonl",
)

SNOWFLAKE_DATABASE = os.getenv(
    "SNOWFLAKE_DATABASE",
    "TESLA_TELEMETRY_DB",
)

SNOWFLAKE_RAW_SCHEMA = os.getenv(
    "SNOWFLAKE_RAW_SCHEMA",
    "RAW",
)

SNOWFLAKE_CURATED_SCHEMA = os.getenv(
    "SNOWFLAKE_CURATED_SCHEMA",
    "CURATED",
)

SNOWFLAKE_TABLE = os.getenv(
    "SNOWFLAKE_TABLE",
    "TESLA_TELEMETRY",
)
