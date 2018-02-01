import json
from model import User
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

    user = User(role = 'Admin', user_name = 'Sumanth', first_name = 'Sumanth', last_name = 'Reddy', phone_number = '+914567890987', email_id = 'sumanth.reddy@incedoinc.com')
    user.save()

    response = {
        "statusCode": 200,
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

def get(event, context):
    body = {
        #"message": "Go Serverless v1.0! Your function executed successfully!",
        "role" : User.get(User.id == 1).role,
        "user_name" : User.get(User.id == 1).user_name,
        "first_name" : User.get(User.id == 1).first_name,
        "last_name" : User.get(User.id == 1).last_name,
        "phone_number" : User.get(User.id == 1).phone_number,
        "email_id" : User.get(User.id == 1).email_id
    }

    response = {
        "statusCode": 200,
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