import json
import pandas as pd
from pprint import pprint as pp



def json_update(path:str, num:str):

    with open(path, 'r') as file:
            data = json.load(file)

    data[num] = num

    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)




def list_to_dataframe(column_name, data):
    
    df = pd.DataFrame({column_name: data})
    return df


def data_frame_into_json(path, data_frame):
    
    with open(path, 'w') as json_file:
        json_file.write(data_frame)
        
        
        
        

