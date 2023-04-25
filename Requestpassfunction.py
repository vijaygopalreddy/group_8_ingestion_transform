import requests
import json

from gcpcsvhunt.gcpcsvhunt import GCPCsvHunt
import csv
import pandas as pd

pathToJsonFile =  './project-pubsub-accesskey.json'
BucketName ='project-pubsub-382822-img'
prefix = ''             # Searches in Outer Directory

obj = GCPCsvHunt(path=pathToJsonFile, bucketName=BucketName)

data = obj.getAllCSV(prefix=prefix)         # Return list of Objects

df1 = data.pop()                            # Pop the First Pandas Object
print(df1.data)   
test=pd.DataFrame(df1.data)                        # Print Pandas Data Frame
json_array = test.to_json(orient='records')
json_object = json.loads(json_array)
print(f'json_array{json_array}')
def send_message_to_google_cloud():
    url = "https://us-central1-project-pubsub-382822.cloudfunctions.net/my_cloud_function"
    data =json_object
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers,timeout=60)
    print(f'r ={r}')

if __name__ == '__main__':
    send_message_to_google_cloud()