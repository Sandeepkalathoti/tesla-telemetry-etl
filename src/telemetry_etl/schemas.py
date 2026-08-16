from dataclasses import dataclass
from datetime import datetime


@dataclass
class TelemetryRecord:
    """Schema representing a Tesla telemetry event."""

    vehicle_id: str
    timestamp: datetime
    speed: float
    battery_level: float
    latitude: float
    longitude: float

    def to_dict(self) -> dict:
        """Convert the telemetry record into a dictionary."""
        return {
            "vehicle_id": self.vehicle_id,
            "timestamp": self.timestamp,
            "speed": self.speed,
            "battery_level": self.battery_level,
            "latitude": self.latitude,
            "longitude": self.longitude,
        }
