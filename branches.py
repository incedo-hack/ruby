import json
from model import Branch
def create(event, context):   
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!", 
        "input" : event       
    }
    for event in event.values():        
        print(event["body"])      
    # address1 = event.input.body.address1
    # address2 = event.input.body.address2
    # state = event.input.body.state
    # city = event.input.body.city
    # zip = event.input.body.zip
    # phone = event.input.body.phone
    # web = event.input.body.web
    # contact_name = event.input.body.contact_name
    # contact_email = event.input.body.contact_email
    branch = Branch(name = 'Incedo Inc', address1 = '248, Udyog Vihar', address2 = 'Phase-IV', state = 'Haryana', city = 'Gurgaon', zip = '122 015', phone = '+91 124 4345400', web = 'www.incedoinc.com', contact_name = 'Chahal', contact_email = 'chahal@incedoinc.com')
    branch.save()

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
    # for event in event.values():
    print(event["pathParameters"].get('id'))
    body = {
        #"message": "Go Serverless v1.0! Your function executed successfully!",
        "name": Branch.get(Branch.id == 1).name,
        "address1" : Branch.get(Branch.id == 1).address1,
        "address2" : Branch.get(Branch.id == 1).address2,
        "state" : Branch.get(Branch.id == 1).state,
        "city" : Branch.get(Branch.id == 1).city,
        "zip" : Branch.get(Branch.id == 1).zip,
        "phone" : Branch.get(Branch.id == 1).phone,
        "web" : Branch.get(Branch.id == 1).web,
        "contact_name" : Branch.get(Branch.id == 1).contact_name,
        "contact_email" : Branch.get(Branch.id == 1).contact_email
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
    data = {
        "input": {            
            "body": " {\r\n \t\"name\": \"hi\",\r\n \t\"address1\": \"hi\",\r\n \t\"address2\": \"hi\",\r\n \t\"state\": \"hi\",\r\n \t\"city\": \"hi\",\r\n \t\"zip\": \"hi\",\r\n \t\"phone\": \"hi\",\r\n \t\"web\": \"hi\",\r\n \t\"contact_name\": \"hi\",\r\n \t\"contact_email\": \"hi\"\r\n }"            
        }            
    }
    print(create(data,None))