import json
from model import User
import logging
import peewee as pw
from peewee import *
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

    role = payload['role'] if 'role' in payload else None
    user_name = payload['user_name'] if 'user_name' in payload else None
    first_name = payload['first_name'] if 'first_name' in payload else None
    last_name = payload['last_name'] if 'last_name' in payload else None
    phone_number = payload['phone_number'] if 'phone_number' in payload else None
    email_id = payload['email_id'] if 'email_id' in payload else None
    account_id = payload['account_id'] if 'account_id' in payload else None
    permissions = payload['permissions'] if 'permissions' in payload else None

    user = User(role = role, user_name = user_name, first_name = first_name, last_name = last_name,\
    phone_number = phone_number, email_id = email_id, account_id = account_id, permissions = permissions)
    user.save()

    response = {
        "statusCode": 200,
        "body": json.dumps(user.id)
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
            user = User.get(id=_id)                   
            response = {
                "statusCode": 200,
                "body": json.dumps(model_to_dict(user))
            }
        except pw.DoesNotExist:
            logger.exception("User detail does not exist for id {}".format(_id))

            body = {
                "message": "User detail does not exist for id {}".format(_id),
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
def getall(event, context):
    users = User.select()
    user_list = []
    for user in users:
        tmp = dict()
        tmp['id'] = user.id
        tmp['user_name'] = user.user_name
        tmp['first_name'] = user.first_name
        tmp['last_name'] = user.last_name
        tmp['phone_number'] = user.phone_number
        tmp['email_id'] = user.email_id
        tmp['account_id'] = user.account_id
        tmp['permissions'] = user.permissions
        user_list.append(tmp)
    response = {
            "statusCode": 200,
            "body": json.dumps(user_list)
        }
    return response


if __name__ == "__main__":
    #print(get(None,None));  
    print(getall(None,None))