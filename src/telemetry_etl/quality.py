from typing import Any


REQUIRED_FIELDS = {
    "vehicle_id",
    "timestamp",
    "speed",
    "battery_level",
    "latitude",
    "longitude",
}


def validate_record(record: dict[str, Any]) -> list[str]:
    """
    Validate a single Tesla telemetry record.

    Returns a list of validation errors.
    An empty list means the record is valid.
    """

    errors: list[str] = []

    missing_fields = REQUIRED_FIELDS - record.keys()

    if missing_fields:
        errors.append(
            f"Missing required fields: {sorted(missing_fields)}"
        )

    if not record.get("vehicle_id"):
        errors.append("vehicle_id must not be empty")

    try:
        speed = float(record["speed"])
        if speed < 0:
            errors.append("speed must be greater than or equal to 0")
    except (KeyError, TypeError, ValueError):
        errors.append("speed must be numeric")

    try:
        battery_level = float(record["battery_level"])
        if not 0 <= battery_level <= 100:
            errors.append(
                "battery_level must be between 0 and 100"
            )
    except (KeyError, TypeError, ValueError):
        errors.append("battery_level must be numeric")

    try:
        latitude = float(record["latitude"])
        if not -90 <= latitude <= 90:
            errors.append(
                "latitude must be between -90 and 90"
            )
    except (KeyError, TypeError, ValueError):
        errors.append("latitude must be numeric")

    try:
        longitude = float(record["longitude"])
        if not -180 <= longitude <= 180:
            errors.append(
                "longitude must be between -180 and 180"
            )
    except (KeyError, TypeError, ValueError):
        errors.append("longitude must be numeric")

    if not record.get("timestamp"):
        errors.append("timestamp must not be empty")

    return errors


def validate_records(
    records: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Separate telemetry records into valid and invalid records.
    """

    valid_records: list[dict[str, Any]] = []
    invalid_records: list[dict[str, Any]] = []

    for record in records:
        errors = validate_record(record)

        if errors:
            invalid_records.append(
                {
                    "record": record,
                    "errors": errors,
                }
            )
        else:
            valid_records.append(record)

    return valid_records, invalid_records
