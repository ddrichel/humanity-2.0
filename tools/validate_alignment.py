import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator,FormatChecker
ROOT=Path(__file__).resolve().parents[1]
def validate_record(record):
    schema=json.loads((ROOT/"schemas/human-alignment.schema.json").read_text())
    Draft202012Validator(schema,format_checker=FormatChecker()).validate(record)
    axes=[item["axis_id"] for item in record["components"]]
    if len(axes)!=len(set(axes)): raise ValueError("axis_id values must be unique")
    actions=[item["action"] for item in record["permission_preferences"]]
    if len(actions)!=len(set(actions)): raise ValueError("permission action values must be unique")
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python tools/validate_alignment.py RECORD.json")
    validate_record(json.loads(Path(sys.argv[1]).read_text()))
    print("Valid alignment record")
