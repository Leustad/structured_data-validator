# Version 3.x
# Usage: $ python main.py

import requests
import json

STRUCTURED_DATA = 'https://search.google.com/structured-data/testing-tool/validate'

urls = {
    # URLs goes here
}


def write_to_file(data):
    try:
        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True, separators=(',', ':'))
    except Exception as e:
        print(e)


# Check for Structured Data Errors
def post_structured_data(url, content_type):
    print('Checking : {}'.format(url))
    resp = requests.post(STRUCTURED_DATA, data=url)
    resp = json.loads(resp.text.replace(")]}'", ''))

    if len(resp['errors']) > 0:
        ctr = 0
        for error in resp['errors']:
            resp['errors'][ctr]['url'] = url
            ctr += 1

        # Write to a file and send e-mail
        print('Found Errors in Structured data.')
        write_to_file(resp['errors'])
    else:
        print('No Errors Found at {}'.format(url))


for url, content_type in urls.items():
    post_structured_data(url, content_type)
