import json
import logging
import peewee as pw
import sys
from model import Utils



logger = logging.getLogger()
logger.setLevel(logging.INFO)

def hello(event, context):
    # foo = main(event, context)
    success = False
    # try:
    #     Utils().setup_tables()
    #     Utils().load_mock_data()
    #     success = True
    # except Exception as exp:
    #     logger.error("Error occured while setting up the tables")
    #     logger.error(exp)

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event,
        "success" : success
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
        row_obj['value'] = row[3].lstrip("-")
        row_obj['path_length'] = row[4]
        row_obj['breadcrumbs'] = row[5]
        # print(row_obj)
        resp.append(row_obj)

    logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
    return resp

def build_tree(items):
    tree = {}    
    for item in items:
        if tree:
            #do something
            new_tree = find_append_parent(tree, item)
        else:
            tree = item
    # print(tree)
    return new_tree

def find_append_parent(tree, item):
    if not 'children' in tree:
        tree['children'] = []
    if tree['id'] == item['parent_id']:
        tree['children'].append(item)
    else:
        for sub_tree in tree['children']:
            find_append_parent(sub_tree, item)
    return tree



foo = main(None, None)
# print(foo)
n_tree = build_tree(foo)
print(json.dumps(n_tree))
