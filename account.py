import json
from model import Account


def create(event, context):
    print("*****HELLO WORLD*****")
    event = {
        "resource": "/accounts",
        "path": "/accounts",
        "httpMethod": "POST",
        "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "CloudFront-Forwarded-Proto": "https",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-Mobile-Viewer": "False",
            "CloudFront-Is-SmartTV-Viewer": "False",
            "CloudFront-Is-Tablet-Viewer": "False",
            "CloudFront-Viewer-Country": "IN",
            "content-type": "application/json",
            "Host": "djvp2idgi0.execute-api.ap-south-1.amazonaws.com",
            "origin": "chrome-extension://fhbjgbiflinjbdggehcddcbncdddomop",
            "postman-token": "c393de21-2cc6-48e4-e920-de02a190266e",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
            "Via": "2.0 a88d0f17b53465837786e5dd493752fa.cloudfront.net (CloudFront)",
            "X-Amz-Cf-Id": "DfChRCECFRetnr7VXSRt-RZFfC3BA0DjoDpv20dPC08L7xZjzY-xRw==",
            "X-Amzn-Trace-Id": "Root=1-5a72c107-0f7152b838e8e2852f1ceb9f",
            "X-Forwarded-For": "14.141.85.52, 54.182.244.103",
            "X-Forwarded-Port": "443",
            "X-Forwarded-Proto": "https"
        },
        "queryStringParameters": None,
        "pathParameters": {
            "id" : "1"
        },
        "stageVariables": None,
        "requestContext": {
            "requestTime": "01/Feb/2018:07:25:59 +0000",
            "path": "/dev/accounts",
            "accountId": "953560108175",
            "protocol": "HTTP/1.1",
            "resourceId": "xi3r9r",
            "stage": "dev",
            "requestTimeEpoch": 1517469959755,
            "requestId": "2695b2fa-0721-11e8-aa52-396125210524",
            "identity": {
                "cognitoIdentityPoolId": None,
                "accountId": None,
                "cognitoIdentityId": None,
                "caller": None,
                "sourceIp": "14.141.85.52",
                "accessKey": None,
                "cognitoAuthenticationType": None,
                "cognitoAuthenticationProvider": None,
                "userArn": None,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36",
                "user": None
            },
            "resourcePath": "/accounts",
            "httpMethod": "POST",
            "apiId": "djvp2idgi0"
        },
        "body": "{\"name\" : \"Incedo Inc\", \r\n\"address1\" : \"KadubeesanaHalli Varthur Hobli\",\r\n \"address2\" : \"Outer Ring road\", \r\n \"state\" : \"Karnataka\", \r\n \"city\" : \"Bangalore\", \r\n \"zip\" : \"560103\", \r\n \"phone\" : \"+918067085800\", \r\n \"web\" : \"www.incedoinc.com\", \"contact_name\" : \"Robert\", \"contact_email\" : \"robert@incedoinc.com\"}",
        "isBase64Encoded": False
    }

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
    
    print(json.loads(event['body'])['name'])
    account = Account(name = json.loads(event['body'])['name'] , address1 = json.loads(event['body'])['address1'], address2 = json.loads(event['body'])['address2'], state = json.loads(event['body'])['state'], city = json.loads(event['body'])['city'], zip = json.loads(event['body'])['zip'], phone = json.loads(event['body'])['phone'], web = json.loads(event['body'])['web'], contact_name = json.loads(event['body'])['contact_name'], contact_email = json.loads(event['body'])['contact_email'])
    account.save()

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
    accountId = event['pathParameters']['id']
    print(accountId)
    body = {
        #"message": "Go Serverless v1.0! Your function executed successfully!",
        "name": Account.get(Account.id == 1).name,
        "address1" : Account.get(Account.id == 1).address1,
        "address2" : Account.get(Account.id == 1).address2,
        "state" : Account.get(Account.id == 1).state,
        "city" : Account.get(Account.id == 1).city,
        "zip" : Account.get(Account.id == 1).zip,
        "phone" : Account.get(Account.id == 1).phone,
        "web" : Account.get(Account.id == 1).web,
        "contact_name" : Account.get(Account.id == 1).contact_name,
        "contact_email" : Account.get(Account.id == 1).contact_email
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
    # print(get(None,None))
    get(None, None)