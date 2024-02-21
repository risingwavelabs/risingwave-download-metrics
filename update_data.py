#!/usr/bin/env python3

import json

# Read json file
with open('counts.json') as f:
    data = json.load(f)
    # Push a new record into data.
    data.append({"date": "2022-01-01", "count": 1})
    # Write the updated data back to the file.
    with open('counts.json', 'w') as f:
        json.dump(data, f)