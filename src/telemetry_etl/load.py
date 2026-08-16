from typing import Any


def prepare_for_load(
    records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """
    Prepare validated telemetry records for loading into Snowflake.

    The function keeps the transformation layer independent
    from the Snowflake connector.
    """

    load_records: list[dict[str, Any]] = []

    for record in records:
        load_records.append(
            {
                "vehicle_id": record["vehicle_id"],
                "timestamp": record["timestamp"],
                "speed": record["speed"],
                "battery_level": record["battery_level"],
                "latitude": record["latitude"],
                "longitude": record["longitude"],
            }
        )

    return load_records
