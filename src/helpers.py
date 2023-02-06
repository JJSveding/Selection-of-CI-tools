import json

import pandas as pd


def read_json_to_dataframe(file_path):
    with open(file_path, 'r', encoding="utf-8") as json_file:
        data = json.load(json_file)
        df = pd.DataFrame(data)
    return df
