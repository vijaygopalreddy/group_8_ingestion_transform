import base64
import json
from google.cloud import pubsub_v1 
import os
    
credentials_path = './project-pubsub-accesskey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path                                 # pip install google-cloud-pubsub

publisher = pubsub_v1.PublisherClient()
PROJECT_ID = os.getenv('project-pubsub-382822')                                 # GOOGLE_CLOUD_PROJECT


def my_cloud_function(request):
    data = request.data
    if data is None:
        print('request.data is empty')
        return ('request.data is empty', 400)

    print(f'request data: {data}')
    data_json = json.loads(data)  
    print(f'request data: {data_json}')
    # topic_path = 'projects/project-pubsub-382822/topics/project-test'  
    topic_path='projects/project-pubsub-382822/topics/jsonPassingData'                # Pubsub topic path
    for obj in data_json:
        print(f'data:{obj}')      
        message_json = json.dumps(obj)
        print(f'data:{obj}')
        message_bytes = message_json.encode('utf-8')
        try:
         publish_future = publisher.publish(topic_path, data=message_bytes)
         publish_future.result()                                         # verify that the publish succeeded
        except Exception as e:
         print(e)
    return "success"
       

