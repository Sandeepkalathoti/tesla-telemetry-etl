import json
from pathlib import Path
from typing import Any

from .config import DATA_FILE


def extract_telemetry(file_path: str = DATA_FILE) -> list[dict[str, Any]]:
    """
    Read Tesla telemetry records from a JSONL file.
    Each line in the file represents one telemetry event.
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Telemetry file not found: {path}")

    records: list[dict[str, Any]] = []

    with path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()

            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(
                    f"Invalid JSON on line {line_number}: {exc}"
                ) from exc

            if not isinstance(record, dict):
                raise ValueError(
                    f"Expected JSON object on line {line_number}"
                )

            records.append(record)

    return records


if __name__ == "__main__":
    telemetry = extract_telemetry()
    print(f"Extracted {len(telemetry)} telemetry records")
