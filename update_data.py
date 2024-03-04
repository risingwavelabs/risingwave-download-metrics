#!/usr/bin/env python3

import json
import sys

# Read json file
with open('count_versioned.json') as f:
    data = json.load(f)
    # Get date from cli args
    date = sys.argv[1]
    osx_count = int(sys.argv[2])
    linux_count = int(sys.argv[3])
    tag_name = sys.argv[4]
    new_record = {
        "date": date,
        "osx_count": osx_count,
        "linux_count": linux_count,
        "tag_name": tag_name
    }
    # Make sure the date is not already in the file
    for record in data:
        if record['date'] == date:
            print(f"Record for {date} already exists")
            sys.exit(0)
    data.append(new_record)

    # Write the updated data back to the file.
    with open('count_versioned.json', 'w') as f:
        json.dump(data, f)