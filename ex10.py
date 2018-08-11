

import requests
import sys
import argparse
import json

parser = argparse.ArgumentParser(description='Get the URL and Destination file to save it\'s contents')

parser.add_argument('url', help='The URL for which content should be seen')
parser.add_argument('dest_file', help='Destination FIle')
parser.add_argument('--content-type', '-c',
        default='html',
        choices=['html','json'],
        help='To specify if its json(j) or html(h)')

args = parser.parse_args()

res = requests.get(args.url)

if res.status_code >= 400:
    print(f"Error Code Received: {res.status_code}")
    sys.exit(1)

if args.content_type == 'json':
    try:
        content = json.dumps(res.json())
        print('It was JSON')
    except ValueError:
        print("Error: Content is not JSON")
        sys.exit(1)
else:
    content = res.text

with open(args.dest_file, 'w', encoding='UTF-8') as f:
    f.write(content)
    print(f"Content written to '{args.dest_file}'")


