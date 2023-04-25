#Importaing the required packages
import base64
import json
from google.cloud import pubsub_v1 # this pubsub package downloading for request passing to pubsub  # pip install google-cloud-pubsub
import os
    
credentials_path = './project-pubsub-accesskey.json' # Project access key manadatory to add request passing files
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path                                

publisher = pubsub_v1.PublisherClient() # initilization of pubsub client 
PROJECT_ID = os.getenv('project-pubsub-382822') # Adding the project id to the environment for identify                          

#writing cloud function for accepting request from post api call  to these function
# And looping the data from json to PUBSUB client
def my_cloud_function(request):
    data = request.data
    if data is None:  #request data null check
        print('request.data is empty')
        return ('request.data is empty', 400)

    print(f'request data: {data}') #printing logs for data identifying from cloud function logs
    data_json = json.loads(data)   #loading json form
    print(f'request data: {data_json}')  #printing logs for proper json
    topic_path='projects/project-pubsub-382822/topics/jsonPassingData' # refering path to pub sub               # Pubsub topic path
    for obj in data_json:
        print(f'data:{obj}')      
        message_json = json.dumps(obj)
        print(f'data:{obj}')
        message_bytes = message_json.encode('utf-8')
        try:
         publish_future = publisher.publish(topic_path, data=message_bytes) # Passing request object to PubSub 
         publish_future.result()                                            # verify that the publish succeeded
        except Exception as e:
         print(e)
    return "success"
       

