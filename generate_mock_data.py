#!/usr/bin/env python3
#
# Generate mock data for testing purposes
# Of the form:
# [
#   { "date": "2019-01-01", "count": 1 },
#   { "date": "2019-01-02", "count": 1 },
#   ...
# ]
#
# USAGE: ./generate_mock_data.py
out_file = 'mock_data.json'
with open(out_file, 'w') as f:
    f.write('[\n')
    for month in range(1, 13):
        for day in range(1, 29):
            f.write(f'  {{ "date": "2019-{month:02d}-{day:02d}", "count": 1 }},\n')
    f.write(f'  {{ "date": "2019-12-29", "count": 1 }}\n')
    f.write(']')
