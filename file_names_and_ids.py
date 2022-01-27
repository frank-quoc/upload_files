import re
import requests
import json
import os

from zipfile import Zipfile 

import file_names_and_ids

zip_file_name_path = "/mnt/c/Users/fho/Documents/BestBath/Concept Quotes.zip"

# insert your api key here
url = "https://api.hubapi.com/crm/v3/imports?hapikey={{}}"


filenames_and_ids = file_names_and_ids.make_dict_of_ids()

def make_dict_of_ids():
    zip_file_name_path = "/mnt/c/Users/fho/Documents/BestBath/Concept Quotes.zip"
    json_ids_path = "/mnt/c/Users/fho/Documents/BestBath/quotes_id.json"

    # Open zip file
    with ZipFile(zip_file_name_path, "r") as zip_obj:
        # Create a list of the filenames
        list_of_files = zip_obj.namelist()
        # This dict will be {key:value} of {file_name: None} at first
        dict_of_files = dict.fromkeys(list_of_files, None)  

        pattern = "^Q-\d{5}"

        with open(json_ids_path) as json_file:
            ids_data = json.load(json_file)[0]

            for file_name in list_of_files:
                # Grab only the "Quote Document Number" from the file name
                result = re.search(pattern, file_name).group(0)
                # Set the dictionary previously to {file_name: Opportunity Internal ID}
                dict_of_files[file_name] = ids_data.get(result, None)
            return {k: v for k, v in dict_of_files.items() if v is not None}


