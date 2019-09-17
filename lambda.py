import logging
import uuid
import time 
import boto3
import json 
import datetime
from boto3.dynamodb.conditions import Key

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client('sns')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    ''' This lambda should send a message if there's no dynamoDB record created by 8pm, 
    if there's record, ignore sending message'''

    now = datetime.datetime.now()
    time_= now.strftime("%Y-%m-%d")
    table = dynamodb.Table('iots')
    response = table.get_item(
    Key={
        'time': time_
    }
    )   
    
    print(response)
    try:
         item = response['Item']
    except KeyError as error:
         print(error)
         item = None
    except TypeError:
         item = None 
    if item != None:
         print('this will also show up in cloud watch')
         logger.info('got event{}'.format(event))
    else:
         print("I should send a message")
         sns.publish(PhoneNumber=phone_number, Message="check on {}")


    logger.info('Received event: ' + json.dumps(event))

    attributes = event['placementInfo']['attributes']
    id = str(uuid.uuid1())
   

    phone_number = attributes['phoneNumber']
    message = attributes['message']

    for key in attributes.keys():
        message = message.replace('{{%s}}' % (key), attributes[key])
    message = message.replace('{{*}}', json.dumps(attributes))

    dsn = event['deviceInfo']['deviceId']
    click_type = event['deviceEvent']['buttonClicked']['clickType']
    message += '\n(DSN: {}, {})'.format(dsn, click_type)
    dynamodb.put_item(TableName='iots', Item={'id':{'S':id}, 'name':{'S':'monitor'}, 'time':{'S':time_}})

    #sns.publish(PhoneNumber=phone_number, Message=message)

    logger.info('SMS has been sent to ' + phone_number)
