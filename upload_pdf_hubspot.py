            
# This example uploads a local file named 'example_file.txt'
# The file is being uploaded to the '/docs' folder
# and will automatically be deleted 3 months after the upload

import requests
import json

import file_names_and_ids

post_url = 'https://api.hubapi.com//files/v3/files'

querystring = {"hapikey":"YOUR_HUBSPOT_API_KEY"}

filename = 'example_file.txt'

file_options = {
    'access': 'PUBLIC_NOT_INDEXABLE',
    "overwrite": False,
    'duplicateValidationStrategy': 'NONE',
    'duplicateValidationScope': 'EXACT_FOLDER'
}

folder = "FOLDERPATH_CONTAINING_FILES"
filename_and_id = file_names_and_ids.make_dict_of_ids()

for filename in filename_and_id:
    filepath = folder + filename
    files_data = {
        'file': (filepath, open(filepath, 'rb'), 'application/pdf'),
        'options': (None, json.dumps(file_options), 'text/strings'),
        'folderPath': (None, '/docs', 'text/strings')
    }

    r = requests.post(post_url, files = files_data, params=querystring)

    print(r)
    print(r.content)