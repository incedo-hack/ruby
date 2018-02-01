import json
import logging
import peewee as pw
import sys

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    foo = main(event, context)
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "foo"  : foo
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

def main(event, context):
    try:
        # rds_host= 'hackathon.cxhkq5lo2z7b.ap-south-1.rds.amazonaws.com'
        rds_host = 'localhost'
        name='root'
        # password='incedoadmin'
        password = 'root'
        db_name = 'rdm'
        # db_name = 'hackathon'
        myDB = pw.MySQLDatabase(db_name, host=rds_host, port=3306, user=name, passwd=password)


        # conn = pymysql.connect(rds_host, user=name,
                            # passwd=password, db=db_name, connect_timeout=5)
    except:
        logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
        sys.exit()

    cursor = myDB.execute_sql("call p_get_tree(1)")
    resp = []
    for row in cursor.fetchall(): 
        # print( row)
        row_obj = dict()
        row_obj['id'] = row[0]
        row_obj['is_deleted'] = row[1]
        row_obj['parent_id'] = row[2]
        row_obj['name'] = row[3].lstrip("-")
        row_obj['path_length'] = row[4]
        row_obj['breadcrumbs'] = row[5]
        # print(row_obj)
        resp.append(row_obj)

    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
    return resp

foo = main(None, None)
print(foo)
