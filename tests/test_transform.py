from datetime import datetime, timezone

from telemetry_etl.transform import transform_telemetry


def test_transform_telemetry():
    records = [
        {
            "vehicle_id": " TESLA001 ",
            "timestamp": "2026-08-15T10:00:00Z",
            "speed": "65.5",
            "battery_level": "82.3",
            "latitude": "17.3850",
            "longitude": "78.4867",
        }
    ]

    result = transform_telemetry(records)

    assert len(result) == 1

    transformed = result[0]

    assert transformed["vehicle_id"] == "TESLA001"
    assert transformed["timestamp"] == datetime(
        2026,
        8,
        15,
        10,
        0,
        tzinfo=timezone.utc,
    )
    assert transformed["speed"] == 65.5
    assert transformed["battery_level"] == 82.3
    assert transformed["latitude"] == 17.3850
    assert transformed["longitude"] == 78.4867


def test_transform_multiple_records():
    records = [
        {
            "vehicle_id": "TESLA001",
            "timestamp": "2026-08-15T10:00:00Z",
            "speed": 65.5,
            "battery_level": 82.3,
            "latitude": 17.3850,
            "longitude": 78.4867,
        },
        {
            "vehicle_id": "TESLA002",
            "timestamp": "2026-08-15T10:01:00Z",
            "speed": 72.1,
            "battery_level": 76.8,
            "latitude": 17.4065,
            "longitude": 78.4772,
        },
    ]

    result = transform_telemetry(records)

    assert len(result) == 2
    assert result[0]["vehicle_id"] == "TESLA001"
    assert result[1]["vehicle_id"] == "TESLA002"
