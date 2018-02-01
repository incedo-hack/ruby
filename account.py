import json
from model import Account
import logging
import peewee as pw
from playhouse.shortcuts import model_to_dict, dict_to_model

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    # body = {
    #     role : value        
    # }
    # from event find pathParameters and extract id from there 
    # if 'event' in event: 
    #     id = event['id']
    # else:
    #     body = {"Error" : "Manditory field ID not provided"}
    #     return response = {
    #     "statusCode": 500,
    #     "body": json.dumps(body)
    # }    
    # user = User.get(User.id == 1)
    # # user = User.get(id=id)
    payload = json.loads(event['body'])

    name = payload['name'] if 'name' in payload else None
    address1 = payload['address1'] if 'address1' in payload else None
    address2 = payload['address2'] if 'address2' in payload else None
    state = payload['state'] if 'state' in payload else None
    city = payload['city'] if 'city' in payload else None
    zip = payload['zip'] if 'zip' in payload else None
    phone = payload['phone'] if 'phone' in payload else None
    web = payload['web'] if 'web' in payload else None
    contact_name = payload['contact_name'] if 'contact_name' in payload else None
    contact_email = payload['contact_email'] if 'contact_email' in payload else None

    account = Account(name = name , address1 = address1, address2 = address2, state = state, \
    city = city, zip = zip, phone = phone, web = web, contact_name = contact_name, contact_email = contact_email)
    account.save()
    # user = User(role = 'Admin', user_name = 'Sumanth', first_name = 'Sumanth', last_name = 'Reddy', phone_number = '+914567890987', email_id = 'sumanth.reddy@incedoinc.com')
    # user.save()

    response = {
        "statusCode": 200,
        "body": json.dumps(account.id)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def get(event, context):
    logging.info("received event %s", event)
    body = {
        #"message": "Go Serverless v1.0! Your function executed successfully!",
        # "role" : User.get(User.id == 1).role,
        # "user_name" : User.get(User.id == 1).user_name,
        # "first_name" : User.get(User.id == 1).first_name,
        # "last_name" : User.get(User.id == 1).last_name,
        # "phone_number" : User.get(User.id == 1).phone_number,
        # "email_id" : User.get(User.id == 1).email_id
    }
    if 'pathParameters' in event and 'id' in event['pathParameters']:
        _id = event['pathParameters']['id']
        try:
            account = Account.get(id=_id)                   
            response = {
                "statusCode": 200,
                "body": json.dumps(model_to_dict(account))
            }
        except pw.DoesNotExist:
            logger.exception("Account detail does not exist for id {}".format(_id))

            body = {
                "message": "Account detail does not exist for id {}".format(_id),
            }
            response = {
                "statusCode": 500,
                "body": json.dumps(body)
            }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
if __name__ == "__main__":
    #print(get(None,None));  
    print(create(None,None))