from telemetry_etl.quality import validate_record, validate_records


def valid_record():
    return {
        "vehicle_id": "TESLA001",
        "timestamp": "2026-08-15T10:00:00Z",
        "speed": 65.5,
        "battery_level": 82.3,
        "latitude": 17.3850,
        "longitude": 78.4867,
    }


def test_valid_record():
    record = valid_record()

    errors = validate_record(record)

    assert errors == []


def test_negative_speed_is_invalid():
    record = valid_record()
    record["speed"] = -10

    errors = validate_record(record)

    assert "speed must be greater than or equal to 0" in errors


def test_invalid_battery_level():
    record = valid_record()
    record["battery_level"] = 120

    errors = validate_record(record)

    assert "battery_level must be between 0 and 100" in errors


def test_invalid_latitude():
    record = valid_record()
    record["latitude"] = 100

    errors = validate_record(record)

    assert "latitude must be between -90 and 90" in errors


def test_invalid_longitude():
    record = valid_record()
    record["longitude"] = 200

    errors = validate_record(record)

    assert "longitude must be between -180 and 180" in errors


def test_missing_vehicle_id():
    record = valid_record()
    record["vehicle_id"] = ""

    errors = validate_record(record)

    assert "vehicle_id must not be empty" in errors


def test_validate_records():
    valid = valid_record()

    invalid = valid_record()
    invalid["speed"] = -5

    valid_records, invalid_records = validate_records(
        [valid, invalid]
    )

    assert len(valid_records) == 1
    assert len(invalid_records) == 1
