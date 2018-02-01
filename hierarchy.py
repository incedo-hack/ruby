import json
import logging
from model import * 
from playhouse.shortcuts import model_to_dict, dict_to_model

def create(event, context):

    payload = json.loads(event['body'])

    name = payload['name'] if 'name' in payload else None
    parent_id = payload['parent_id'] if 'parent_id' in payload else None
    account_id = payload['account_id'] if 'account_id' in payload else None
    branch_id = payload['branch_id'] if 'branch_id' in payload else None
    type = payload['type'] if 'type' in payload else None


    # body = {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "input": event
    # }

    prefixNodes = prefix_nodes(name = name, parent_id = parent_id, account_id = account_id,\
     branch_id=branch_id, type=type)
     
    prefixNodes.save()
    response = {
        "statusCode": 200,
        "body": json.dumps(model_to_dict(prefixNodes))
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
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    if 'pathParameters' in event and 'id' in event['pathParameters']:
        _id = event['pathParameters']['id']
        tree_list = query_db(_id)
        if tree_list:
            tree_json = build_tree(tree_list)
            body = tree_json
        else:
            body = {
                "message": "No data found for the given pathParameters",
                "input": event,
                "query_output" : tree_list
            }
            response = {
                "statusCode": 400,
                "body": json.dumps(body)
            }
            return response
        
    else:
        body = {
            "message": "Error no id in pathParameters",
            "input": event
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


# @classmethod
def query_db(id):
    if not id:
        id = 1
    # cursor = database.execute_sql("call p_get_tree(1)")
    cursor = database.execute_sql("call p_get_tree(%s)" %(id))
    response = []
    for row in cursor.fetchall(): 
        row_obj = dict()
        row_obj['id'] = row[0]
        row_obj['is_deleted'] = row[1]
        row_obj['parent_id'] = row[2]
        row_obj['value'] = row[3].lstrip("-")
        row_obj['path_length'] = row[4]
        row_obj['breadcrumbs'] = row[5]
        # print(row_obj)
        response.append(row_obj)
    return response

# @classmethod
def build_tree(items):
    '''
     Function to build tree
    '''
    tree = {}    
    for item in items:
        if tree:
            #do something
            tree = find_append_parent(tree, item)
        else:
            tree = item
    # print(tree)
    return tree

# @classmethod
def find_append_parent(tree, item):
    '''
    find parent and append child to it
    '''
    if not 'children' in tree:
        tree['children'] = []
    if tree['id'] == item['parent_id']:
        tree['children'].append(item)
    else:
        for sub_tree in tree['children']:
            find_append_parent(sub_tree, item)
    return tree
