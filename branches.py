import json
from model import Branch
import logging
from playhouse.shortcuts import model_to_dict, dict_to_model

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create(event, context):   
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!", 
        "input" : event       
    }
    # for event in event.values():        
    #     print(event["body"])       

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

    branch = Branch(name = name , address1 = address1, address2 = address2, state = state, \
    city = city, zip = zip, phone = phone, web = web, contact_name = contact_name, \
    contact_email = contact_email)    
    branch.save()

    response = {
        "statusCode": 200,
        "body": json.dumps(branch.id)
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
        # "name": Branch.get(Branch.id == 1).name,
        # "address1" : Branch.get(Branch.id == 1).address1,
        # "address2" : Branch.get(Branch.id == 1).address2,
        # "state" : Branch.get(Branch.id == 1).state,
        # "city" : Branch.get(Branch.id == 1).city,
        # "zip" : Branch.get(Branch.id == 1).zip,
        # "phone" : Branch.get(Branch.id == 1).phone,
        # "web" : Branch.get(Branch.id == 1).web,
        # "contact_name" : Branch.get(Branch.id == 1).contact_name,
        # "contact_email" : Branch.get(Branch.id == 1).contact_email
    }

    if 'pathParameters' in event and 'id' in event['pathParameters']:
        _id = event['pathParameters']['id']
        try:
            branch = Branch.get(id=_id)
            logger.info("find branch ")          
        
            response = {
                "statusCode": 200,
                "body": json.dumps(model_to_dict(branch))
            }
        except Exception as exp:
            logger.exception(exp)

            body = {
                "message": "Somethign went wrong",
                 "exception" : exp
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
    data = {
        "input": {            
            "body": " {\r\n \t\"name\": \"hi\",\r\n \t\"address1\": \"hi\",\r\n \t\"address2\": \"hi\",\r\n \t\"state\": \"hi\",\r\n \t\"city\": \"hi\",\r\n \t\"zip\": \"hi\",\r\n \t\"phone\": \"hi\",\r\n \t\"web\": \"hi\",\r\n \t\"contact_name\": \"hi\",\r\n \t\"contact_email\": \"hi\"\r\n }"            
        }            
    }
    print(create(data,None))