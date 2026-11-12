
#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
from pathlib import Path

DIRECTORIES = ["rules", "decoders"]

def main():
    errors = []
    checked = 0

    for directory in DIRECTORIES:
        for path in Path(directory).rglob("*.xml"):
            checked += 1

            try:
                ET.parse(path)
                print(f"[PASS] {path}")

            except ET.ParseError as error:
                errors.append(f"{path}: {error}")

    print(f"\nXML files checked: {checked}")

    if errors:
        print("\nXML validation failed:")

        for error in errors:
            print(f"[ERROR] {error}")

        sys.exit(1)

    print("XML validation successful.")

if __name__ == "__main__":
    main()
