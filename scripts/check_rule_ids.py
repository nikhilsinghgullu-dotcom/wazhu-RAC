
#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

RULES_DIR = Path("rules")

def main():
    rule_ids = defaultdict(list)
    errors = []

    for path in RULES_DIR.rglob("*.xml"):
        try:
            tree = ET.parse(path)
            root = tree.getroot()

            for rule in root.iter("rule"):
                rule_id = rule.get("id")

                if rule_id:
                    rule_ids[rule_id].append(str(path))

        except ET.ParseError as error:
            errors.append(f"{path}: {error}")

    duplicates = {
        rule_id: files
        for rule_id, files in rule_ids.items()
        if len(files) > 1
    }

    if errors:
        for error in errors:
            print(f"[ERROR] {error}")

    if duplicates:
        print("\nDuplicate Wazuh rule IDs found:")

        for rule_id, files in duplicates.items():
            print(f"\nRule ID: {rule_id}")

            for file in files:
                print(f"  - {file}")

        sys.exit(1)

    if errors:
        sys.exit(1)

    print(f"Checked {len(rule_ids)} unique Wazuh rule IDs.")
    print("No duplicate rule IDs found.")

if __name__ == "__main__":
    main()
