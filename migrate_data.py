#!/usr/bin/env python3

import json
import sys

# Read json file
with open('counts.json') as f:
    data = json.load(f)
    # Get date from cli args
    for record in data:
        if record['date'] == "2024-03-01":
            record['tag_name'] = "v1.7.0"t s
        else:
            record['tag_name'] = "v1.6.1"

    # Write the updated data back to the file.
    with open('counts.json', 'w') as f:
        json.dump(data, f)