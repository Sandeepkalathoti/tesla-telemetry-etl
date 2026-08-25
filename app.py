from flask import Flask, jsonify
from flask_cors import CORS

from src.telemetry_etl.extract import extract_telemetry
from src.telemetry_etl.transform import transform_telemetry
from src.telemetry_etl.quality import validate_records
from src.telemetry_etl.load import prepare_for_load


app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Tesla Telemetry ETL Pipeline API is running"
        }
    )


@app.route("/run-pipeline", methods=["POST"])
def run_pipeline():
    try:

        # STEP 1: EXTRACT
        raw_records = extract_telemetry()

        # STEP 2: TRANSFORM
        transformed_records = transform_telemetry(
            raw_records
        )

        # STEP 3: DATA QUALITY
        valid_records, invalid_records = validate_records(
            transformed_records
        )

        # STEP 4: PREPARE FOR LOAD
        load_records = prepare_for_load(
            valid_records
        )

        return jsonify(
            {
                "status": "success",
                "pipeline": {
                    "extract": {
                        "records_extracted": len(raw_records)
                    },
                    "transform": {
                        "records_transformed": len(
                            transformed_records
                        )
                    },
                    "quality": {
                        "valid_records": len(
                            valid_records
                        ),
                        "invalid_records": len(
                            invalid_records
                        )
                    },
                    "load": {
                        "records_prepared_for_load": len(
                            load_records
                        )
                    }
                },
                "sample_record": (
                    load_records[0]
                    if load_records
                    else None
                )
            }
        )

    except Exception as error:

        return jsonify(
            {
                "status": "error",
                "message": str(error)
            }
        ), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
