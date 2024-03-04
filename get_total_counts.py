#!/usr/bin/env python3

import json
import sys

# Read json file
with open('count_versioned.json') as f:
    data = json.load(f)
    versions = None
    # Ordered list of versions TODO: automatically get this from github.
    with open('versions.json') as vf:
        versions = json.load(vf)

    version_to_index = {}
    for i in range(len(versions)):
        version_to_index[versions[i]] = i

    total_osx_count_per_version = {}
    total_linux_count_per_version = {}
    for version in versions:
        total_osx_count_per_version[version] = 0
        total_linux_count_per_version[version] = 0

    for record in data:
        # It's ordered, we are just getting the last record for each version,
        # That contains the total count.
        total_osx_count_per_version[record['tag_name']] = record['osx_count']
        total_linux_count_per_version[record['tag_name']] = record['linux_count']

    # Make sure to get the accumulated count for each version.
    for i in range(len(versions)):
        if i > 0:
            total_osx_count_per_version[versions[i]] += total_osx_count_per_version[versions[i-1]]
            total_linux_count_per_version[versions[i]] += total_linux_count_per_version[versions[i-1]]

    # Finally, compute the total downloads overtime across all versions.
    total_data = []
    for record in data:
        version_index = version_to_index[record['tag_name']]
        new_record = None
        if version_index > 0:
            previous_version = versions[version_index-1]
            new_record = {
                'date': record['date'],
                'osx_count': record['osx_count'] + total_osx_count_per_version[previous_version],
                'linux_count': record['linux_count'] + total_linux_count_per_version[previous_version],
            }
        else:
            new_record = {
                'date': record['date'],
                'osx_count': record['osx_count'],
                'linux_count': record['linux_count'],
            }

        total_data.append(new_record)

    # Write the updated data back to the file.
    with open('counts.json', 'w') as cf:
        json.dump(total_data, cf)