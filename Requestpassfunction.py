import requests
import json
#Adding one more efficient package for converting csv to json 
from gcpcsvhunt.gcpcsvhunt import GCPCsvHunt
import csv
import pandas as pd

pathToJsonFile =  './project-pubsub-accesskey.json' #Proving key file path for access
bucketName ='project-pubsub-382822-img'  #Providing bucket path
prefix = ''             # Searches in Outer Directory

objectInfo = GCPCsvHunt(path=pathToJsonFile, bucketName=bucketName) #Accessing cloud bucket file with key json

data = objectInfo.getAllCSV(prefix=prefix)         # Return list of Objects

dataFrameFileInfo = data.pop()                      # Pop the First Pandas Object
print(dataFrameFileInfo.data)   
formatedData=pd.DataFrame(dataFrameFileInfo.data)    # Print Pandas Data Frame
jsonArray = formatedData.to_json(orient='records')   # Converting json string
json_object = json.loads(jsonArray)                  # Loading Json object
print(f'json_array{jsonArray}')                      # loging json object for references
# Calling function with filename.python
#Then calling Post Api of cloud function 
#Passing request conversion CSV file JSON data to cloud function end point
def send_message_to_google_cloud():
    url = "https://us-central1-project-pubsub-382822.cloudfunctions.net/my_cloud_function"
    data =json_object
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers,timeout=60)
    print(f'r ={r}')
# function declaring
if __name__ == '__main__':
    send_message_to_google_cloud()