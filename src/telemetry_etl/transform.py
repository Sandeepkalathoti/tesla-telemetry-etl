from datetime import datetime
from typing import Any


def transform_telemetry(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Clean and standardize Tesla telemetry records.
    """

    transformed_records: list[dict[str, Any]] = []

    for record in records:
        vehicle_id = str(record["vehicle_id"]).strip()

        timestamp = datetime.fromisoformat(
            record["timestamp"].replace("Z", "+00:00")
        )

        transformed_record = {
            "vehicle_id": vehicle_id,
            "timestamp": timestamp,
            "speed": float(record["speed"]),
            "battery_level": float(record["battery_level"]),
            "latitude": float(record["latitude"]),
            "longitude": float(record["longitude"]),
        }

        transformed_records.append(transformed_record)

    return transformed_records
